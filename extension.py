#!/usr/bin/env python3
"""
Run the attack set against your service.  <- UNIT 8, MILESTONE 2

    python app.py                                   # in one terminal
    python  extension.py --set path/to/attack_set  # in another

    python  extension.py --set ... --label before
    python  extension.py --set ... --label after   # after your improvement

"""

import argparse
import csv
import datetime as dt
import json
import sys
from pathlib import Path

import config

# Windows consoles often run a codepage that can't print every character in
# this file's help text. Without this, `--help` ends in a UnicodeEncodeError
# traceback instead of the help — which is a miserable first thing to hit.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(errors="replace")
    except (AttributeError, ValueError):  # not a normal text stream
        pass


DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"


def load_attacks(folder: Path):
    """
    Read both attack files. Returns (attacks, problems).

    A row that won't parse is skipped and reported rather than raising. One
    stray comma in a file you didn't write should cost you that attack, not
    every other attack in the set.

    `attacks_malformed_requests.csv` may carry two optional columns:

        send_as       `json` (default) parses raw_body and sends it as JSON.
                      `raw` sends raw_body's bytes exactly as written — which
                      is the only way to send JSON that doesn't parse, or an
                      empty body.
        content_type  what to claim it is. Defaults to application/json.
    """
    attacks, problems = [], []

    text_file = folder / "attacks.csv"
    if text_file.exists():
        with text_file.open(encoding="utf-8") as f:
            for n, row in enumerate(csv.DictReader(f), 2):
                try:
                    attacks.append({
                        "id": row["id"],
                        "family": row["family"],
                        "targets": row["targets"],
                        "body": {"text": row["text"],
                                 "creator_id": f"attacker_{row['id']}"},
                    })
                except (KeyError, TypeError) as exc:
                    problems.append(f"attacks.csv line {n}: {exc}")

    request_file = folder / "attacks_malformed_requests.csv"
    if request_file.exists():
        with request_file.open(encoding="utf-8") as f:
            for n, row in enumerate(csv.DictReader(f), 2):
                try:
                    attack = {
                        "id": row["id"],
                        "family": row["family"],
                        "targets": row["targets"],
                    }
                    if (row.get("send_as") or "json").strip().lower() == "raw":
                        attack["raw"] = row["raw_body"]
                        attack["content_type"] = (
                            row.get("content_type") or "application/json"
                        )
                    else:
                        attack["body"] = json.loads(row["raw_body"])
                    attacks.append(attack)
                except (KeyError, TypeError, json.JSONDecodeError) as exc:
                    problems.append(
                        f"attacks_malformed_requests.csv line {n}: {exc}. "
                        f"If the body is meant to be unparseable, set send_as=raw."
                    )

    return attacks, problems


def send(url, attack, timeout):
    """
    One request. Returns (status_code, parsed_body_or_none, error_or_none).

    A crash on the far end is a result, not a reason to stop — the stop rule
    for this milestone is explicit that a service dying partway through is
    something to record and keep going from.
    """
    import requests

    try:
        if "raw" in attack:
            response = requests.post(
                f"{url}/submit",
                data=attack["raw"].encode("utf-8"),
                headers={"Content-Type": attack["content_type"]},
                timeout=timeout,
            )
        else:
            response = requests.post(f"{url}/submit", json=attack["body"],
                                     timeout=timeout)
    except Exception as exc:  # noqa: BLE001
        return None, None, f"{type(exc).__name__}: {exc}"

    try:
        return response.status_code, response.json(), None
    except ValueError:
        return response.status_code, None, f"response wasn't JSON: {response.text[:200]}"


def send_samples(url, timeout):
    """
    One request. Returns (status_code, parsed_body_or_none, error_or_none).
    """
    import requests

    filepaths = ['samples/frankenstein.json', 'samples/jabberwocky.json', 'samples/gatsby.json']

    responses = []

    for path in filepaths:
        with open(path, "rb") as file:
            payload = json.load(file)
            response = requests.post(f"{url}/submit", json=payload, timeout=timeout)
            responses.append([path, response.json()])

    return responses


def warn_about_rate_limits(attacks, health):
    """
    Some attacks only mean something against a limiter that's switched on.

    Run those with rate limiting off and every one comes back `200`, which
    reads exactly like the attack failing to get through — the most
    misleading result this tool can produce, because it looks like a pass.
    So say so before the run rather than after.
    """
    needs_limits = sorted({a["family"] for a in attacks
                           if "flood" in a["family"]})
    if not needs_limits:
        return
    if health.get("rate_limiting"):
        return

    print("\n" + "!" * 60, file=sys.stderr)
    print(f"The service says rate limiting is OFF, and this set contains "
          f"{', '.join(needs_limits)}.", file=sys.stderr)
    print("Those attacks will all come back 200 because nothing is counting "
          "them — which\nlooks like they were stopped, and is the opposite of "
          "what it means.", file=sys.stderr)
    print("\nTurn the limiter on first (Milestone 1), then re-run.",
          file=sys.stderr)
    print("!" * 60 + "\n", file=sys.stderr)


def curl_commands(url, attack):
    """
    (bash, windows) — the same request, written for both shells.

    RUNNING.md already says PowerShell needs `curl.exe` on one line with the
    inner quotes backslashed, so print that variant too rather than making
    half the room translate it live.
    """
    if "raw" in attack:
        body = attack["raw"]
        content_type = attack["content_type"]
    else:
        body = json.dumps(attack["body"])
        content_type = "application/json"

    # Inside bash's single quotes an apostrophe has to close the quote, escape
    # itself and reopen — '\'' — and several attacks contain one.
    bash_body = body.replace("'", "'\\''")
    bash = (f"curl -X POST {url}/submit \\\n"
            f'  -H "Content-Type: {content_type}" \\\n'
            f"  -d '{bash_body}'")

    # PowerShell wants the JSON's own double quotes backslashed, and doubles an
    # apostrophe to keep it inside the single-quoted string.
    windows_body = body.replace('"', '\\"').replace("'", "''")
    windows = (f"curl.exe -X POST {url}/submit "
               f'-H "Content-Type: {content_type}" '
               f"-d '{windows_body}'")

    return bash, windows


# Past this, a curl command is longer than a terminal or a projector can show
# and pasting it is worse than letting the script send it.
CURL_TOO_LONG = 2000


def require_requests():
    """The one dependency the sending paths need, checked before they start."""
    try:
        import requests  # noqa: F401
    except ImportError:
        print("The `requests` package isn't installed.\n"
              "Run: pip install -r requirements.txt", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--set", dest="folder",
                        help="folder holding attacks.csv")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--timeout", type=float, default=90.0,
                        help="seconds per request — signal one runs a model, so be generous")
    parser.add_argument("--id", dest="attack_id", metavar="ID",
                        help="run only the attack with this id, e.g. EV03")
    parser.add_argument("--show", action="store_true",
                        help="print the selected attack(s) and a curl command for "
                             "each instead of sending anything")
    args = parser.parse_args()

    print("CRITERION 1 AND 5:")
    print()

    if not args.folder:
        print("Give me an attack set: --set path/to/folder\n"
              "Or test your rate limit instead: --flood 15", file=sys.stderr)
        sys.exit(1)

    folder = Path(args.folder)
    attacks, problems = load_attacks(folder)
    if problems:
        print(f"{len(problems)} row(s) in the attack set wouldn't parse and were "
              f"SKIPPED:", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        print("Say so in your write-up — a skipped row is a gap in your run.\n",
              file=sys.stderr)
    if not attacks:
        print(f"No attack files found in {folder}.\n"
              f"Expected attacks.csv — check the path.", file=sys.stderr)
        sys.exit(1)

    require_requests()
    import requests
    try:
        health = requests.get(f"{args.url}/health", timeout=5).json()
    except Exception:  # noqa: BLE001
        print(f"Nothing answering at {args.url}.\n"
              f"Start your service first:  python app.py", file=sys.stderr)
        sys.exit(1)

    warn_about_rate_limits(attacks, health)

    print(f"{len(attacks)} attacks against {args.url}")
    print("Signal one runs a model. The first request is slow while it loads;\n"
          "after that, a second or two each.\n")

    for i, attack in enumerate(attacks, 1):
        status, payload, error = send(args.url, attack, args.timeout)
        
        print(f"  [{i:>2}/{len(attacks)}]     {attack['id']:<6}     {attack['family']:<17} ")
        print(f"  status: {status}")
        print(f"  payload: {payload}")
        print(f"  error: {error}")
        print()

    print("CRITERION 2:")
    print()

    c2 = True

    responses = send_samples(args.url, args.timeout)
    for response in responses:
        print(f"FILE: {response[0]}:")
        print(response[1])
        print()

        if response[1]['time_taken'] > 10:
            c2 = False

    print(f"MET CRITERION 2: {c2}")
    print()
    print()

    print("CRITERION 3 and 4:")
    print()

    log = response[1]

    print('unsuccessful appeal: non existant content id')
    print(requests.post(f"{args.url}/appeal", json={'content_id': log['content_id'][:-2], 'reasoning': 'stated reason'}))
    print()

    print('successful appeal')
    successful_appeal = requests.post(f"{args.url}/appeal", json={'content_id': log['content_id'], 'reasoning': 'stated reason'})
    print(successful_appeal)
    successful_appeal = successful_appeal.json()
    print()

    print('appeal status:')
    print(requests.get(f"{args.url}/status", json={'appeal_id': successful_appeal['appeal_id']}).json())
    print()

    print('unsuccessful decision: non existant content id')
    print(requests.post(f"{args.url}/decide", json={'content_id': log['content_id'][:-2], 
                                                    'appeal_id': successful_appeal['appeal_id'], 
                                                    'verdict': 'overturned', 'decision': 'human'}))
    print()

    print('unsuccessful decision: non existant appeal id')
    print(requests.post(f"{args.url}/decide", json={'content_id': log['content_id'], 
                                                    'appeal_id': successful_appeal['appeal_id'][:-2], 
                                                    'verdict': 'overturned', 'decision': 'human'}))
    print()

    print('successful decision: without notes')
    print(requests.post(f"{args.url}/decide", json={'content_id': log['content_id'], 
                                                    'appeal_id': successful_appeal['appeal_id'], 
                                                    'verdict': 'overturned', 'decision': 'human'}))
    print()

    print('successful decision: with notes')
    print(requests.post(f"{args.url}/decide", json={'content_id': log['content_id'], 
                                                    'appeal_id': successful_appeal['appeal_id'], 
                                                    'verdict': 'overturned', 'decision': 'human', 
                                                    'notes': 'some notes'}))
    print()

    print('appeal status:')
    print(requests.get(f"{args.url}/status", json={'appeal_id': successful_appeal['appeal_id']}).json())







if __name__ == "__main__":
    main()
