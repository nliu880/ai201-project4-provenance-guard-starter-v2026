#!/usr/bin/env python3
"""
Provenance Guard — the web service.

    python app.py

Then, in another terminal:

    curl -X POST http://127.0.0.1:5000/ping \
      -H "Content-Type: application/json" \
      -d '{"message": "hello"}'

That's the example route. It works right now, before you've written anything.
**Leave it alone** — it's your control. When something breaks later, check that
`/ping` still answers: if it does, the problem is in your handler; if it
doesn't, it's the service itself.

Routes:

    POST /ping        the worked example. Already works. Don't edit it
    POST /submit      ← YOU BUILD THIS (Milestone 3, 4, 5)
    POST /appeal      ← YOU BUILD THIS (Milestone 5)
    GET  /log         the audit log. Already works
    GET  /health      is the service up, and is the model loaded
"""

import uuid

from flask import Flask, jsonify, request

import audit
import config

import regex as re
from datetime import datetime, timezone

app = Flask(__name__)


# ── Rate limiting — UNIT 8 ────────────────────────────────────────────────────
# Off until you turn it on. In unit 8, Milestone 1:
#
#   1. Set RATE_LIMITING_ENABLED = True in config.py (or AI201_RATE_LIMITS=1)
#   2. Choose your numbers there
#   3. Uncomment the @limiter.limit(...) line on /submit below
#
# The order doesn't matter. While limiting is off, that decorator is a no-op
# that quietly does nothing, so uncommenting it early costs you nothing — but
# it also means no 429 until you've done step 1.
#
# The storage backend is preconfigured, which stops Flask-Limiter printing a
# warning on every start. In-memory is right for one laptop and wrong for
# anything real — a restart forgets every count.

class _LimiterOff:
    """
    Stands in for the real limiter while rate limiting is off.

    It makes @limiter.limit(...) a decorator that returns the route
    untouched, so uncommenting the line before you flip the setting is
    harmless instead of a crash on startup.
    """

    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()
if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        """
        Who a request counts against.

        Falling back to the caller's address is the easy version. Unit 8's
        stretch asks about per-creator limits instead — and the difference
        matters: one script can look like a thousand callers, and one household
        can look like one.
        """
        payload = request.get_json(silent=True)
        # A body that parses as JSON but isn't an object — a bare list or
        # string — has no .get. Without this guard the key function raises
        # BEFORE the route runs, and a malformed request becomes a 500 that
        # looks like your handler crashed when your handler never ran.
        if not isinstance(payload, dict):
            return get_remote_address()
        creator = payload.get("creator_id")
        return creator if isinstance(creator, str) and creator.strip() else get_remote_address()

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):
        """
        A rejected request still leaves a trace.

        ⚠️ An attack that shows up only as an absence is one you'll never find.
        """
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            payload = {}
        audit.log_rejection(
            creator_id=payload.get("creator_id", "unknown"),
            reason="rate_limited",
            limit=str(exc.description),
        )
        return jsonify({
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }), 429


# ── The worked example. Already works. Don't edit. ────────────────────────────

@app.post("/ping")
def ping():
    """
    Everything a route needs, in six lines.

    JSON arrives as a dict. You pull things out of it. You return a dict and
    the framework turns it into a response. That's the whole idea.
    """
    payload = request.get_json(silent=True) or {}
    return jsonify({
        "ok": True,
        "you_sent": payload.get("message"),
        "service": "provenance-guard",
    })


@app.get("/health")
def health():
    """Is the service up, and has the model been downloaded yet?"""
    import detector

    loaded = detector._model is not None
    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": loaded,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "log_entries": len(audit.read_entries()),
    })


# ── YOU BUILD THIS ────────────────────────────────────────────────────────────

@app.post("/submit")
# @limiter.limit(f"{config.RATE_LIMIT_PER_MINUTE}/minute;{config.RATE_LIMIT_PER_DAY}/day")
def submit():
    """
    Take a piece of text, decide about it, log the decision, answer.

    Expects JSON:
        {"text": "...", "creator_id": "..."}

    Should return JSON with, at minimum:
        {"content_id": "...", "guess": "...", "confidence": 0.0, "label": "...",
         "model_score": 0.0, "style_score": 0.0}

    ⚠️ **Both signal scores go in the response, not just the log.** Unit 8's
    `run_attacks.py` and `run_eval.py` read `model_score` and `style_score`
    straight off this response and put them in your reports. Leave them out and
    every row of next unit's evidence says `null` — which is exactly the
    diagnostic you need to name a stage and a mechanism. You do not want to
    find that out after running the attack set.

    ─────────────────────────────────────────────────────────────────────────
    Build it in three passes. Do not skip ahead — the ordering is how you tell
    a broken route from a broken signal.

    **Milestone 3 — the route answers.**
      1. Return a hardcoded response. Confirm `curl` gets it back before you
         add any logic at all.
      2. Then pull `text` and `creator_id` out of the payload.
      3. Then call ONE signal — `detector.model_signal(text)` — and put the
         real number in. Leave confidence and label as placeholders.
      4. Log every submission with `audit.log_decision(...)`. The content_id
         matters: `/appeal` needs it, and a student who skips it rebuilds this
         whole flow later.

    **Milestone 4 — the second signal and the score.**
      5. Add `stylometry.style_signal(text)`.
      6. Combine them with `scoring.combine_signals(...)`.
      7. Log BOTH signal scores alongside the combined one, and put them in the
         response too. Next unit you can't diagnose anything without them.

    **Milestone 5 — the label.**
      8. `scoring.score_to_label(...)` and put the real label in the response.

    ─────────────────────────────────────────────────────────────────────────
    Worth deciding early, because unit 8's attack set will decide it for you:
    what should this do when `text` is missing, empty, or enormous? A crash on
    a malformed input is one of the most common real failures there is.
    """

    import detector
    import stylometry
    import scoring

    payload = request.get_json(silent=True) or {}
    text = payload.get("text") or {}

    if not isinstance(text, str) or not text.strip(): # empty json
        return jsonify({
            "error": "bad_request", 
            "message": 'Send properly formatted JSON with a non-empty "text" and "creator_id".'
            }), 400

    error_msg = jsonify({
            "error": "bad_request", 
            "message": "This model currently only supports English words and letters. Please do not use other languages or type in only punctuation or numbers."
            }), 400
    
    text = re.sub(r"\n", " ", text)
    
    if re.search(r"[[:cntrl:]]", text): # control characters
        print('control chars')
        return error_msg
    elif len(re.findall(r"\p{P}| |\d|\p{Emoji}", text)) == len(text): # all punctuation or all digits all emoji or some weird combo of that
        print('all punc or emoji or digits')
        return error_msg
    elif len(re.findall(r"[^a-zA-Z\s\d\p{P}\n=<>]", text)) > 0: # not english
        print('not english?')
        return error_msg

    if len(stylometry.words(text)) < 2 or len(stylometry.words(text)) >= 750: # too short or too long
        return jsonify({
            "error": "bad_request", 
            "message": "Text is either too short or too long (one word or over 750 words)."
            }), 400
    
    content_id = f"c_{uuid.uuid4().hex[:12]}"
    creator_id = payload.get("creator_id") or None

    if not isinstance(creator_id, str):
        return jsonify({
            "error": "bad_request", 
            "message": "Please include a creator_id as plain text."
            }), 400

    model_score = detector.model_signal(text)
    style_score = stylometry.style_signal(text)
    combined = scoring.combine_signals(model_score, style_score)
    confidence = 1 - abs(model_score - style_score) / max(model_score, style_score)
    guess, label = scoring.score_to_label(combined)

    audit.log_decision(
        content_id=content_id,
        creator_id=creator_id,
        guess=guess,
        model_score=model_score,
        style_score=style_score,
        combined_score=combined,
        label=label,
        status="decided",
        confidence=confidence,
        text=text,
    )

    return jsonify({
        "content_id": content_id, 
        "creator_id": creator_id, 
        "guess": guess,
        "model_score": model_score, 
        "style_score": style_score,
        "combined_score": combined,
        "label": label,
        "confidence": combined,
    }), 200


@app.post("/appeal")
def appeal():
    """
    A writer says you got it wrong. 

    Expects JSON:
        {"content_id": "...", "reasoning": "..."}

    Should:
      1. Check the content_id actually exists — `audit.entries_for(id)` tells
         you. A typo here fails silently and looks like a broken endpoint,
         which is the single most common way this milestone eats an hour.
      2. Record the appeal with `audit.log_appeal(...)`, which moves the item
         to `under_review`.
      3. Confirm to the writer. No automatic re-checking needed.

    This is the smallest endpoint in the project and the one that matters most
    to the person on the other end. It's the only thing standing between a
    wrong accusation and nothing at all.
    """
    payload = request.get_json(silent=True) or {}
    
    content_id = payload.get("content_id", "unknown")
    content = audit.entries_for(content_id)
    
    if len(content) == 0:
        return jsonify({
            "error": "bad_request", 
            "message": "content_id does not exist."
            }), 400

    reasoning = payload.get("reasoning")
    creator_id = content[0].get("creator_id")
    appeal_id = f"c_{uuid.uuid4().hex[:12]}"
    audit.log_appeal(content_id, creator_id, reasoning, appeal_id)

    return jsonify({
        "content_id": content_id,
        "creator_id": creator_id,
        "confirmation": "Appeal received.",
        "appeal_id": appeal_id,
    }), 200


@app.get("/status")
def status():
    """
    Expects {'content_id': ...}

    Check appeal status.

    """
    payload = request.get_json(silent=True) or {}
    
    content_id = payload.get("content_id", "unknown")
    content = audit.entries_for(content_id)
    
    if len(content) == 0:
        return jsonify({
            "error": "bad_request", 
            "message": "content_id does not exist."
            }), 400

    if content[-1].get("status") == 'final decision':
        return jsonify({
            "content_id": content_id,
            "status": 'decision appealed and decided',
            "decision": content[-1].get("decision")
        }), 200
    elif content[-1].get("status") == 'under_review':
        return jsonify({
            "content_id": content_id,
            "status": 'under review'
        }), 200
    elif content[-1].get("status") == 'decided':
        return jsonify({
            "content_id": content_id,
            "status": 'initial decision'
        }), 200

@app.get("/review")
def review():
    """
    Expects {'appeal_id': ...}
    
    Gets appeal and original decision for a reviewer to check.

    """
    payload = request.get_json(silent=True) or {}
    
    appeal_id = payload.get("appeal_id", "unknown")
    appeal = audit.entries_for(appeal_id, True)
    
    if len(appeal) == 0:
        return jsonify({
            "error": "bad_request", 
            "message": "appeal_id does not exist."
            }), 400

    content_id = appeal[0].get('content_id')
    content = audit.entries_for(content_id)[0]

    return [appeal, content], 200

@app.post("/decide")
def decide():
    """
    Expects {'content_id', ..., 'appeal_id': ..., 'verdict':, ..., 'decision': ..., 'notes':, ...}. 
    'reviewer_id' (for the future)

    Logs a decision made by a reviewer, which can be anyone as of now (11/11/2026). 
    Maybe this will be fixed in the future.
    """

    payload = request.get_json(silent=True) or {}
    
    content_id = payload.get("content_id", "unknown")
    appeal_id = payload.get("appeal_id", "unknown")
    appeals = audit.entries_for(appeal_id, True)
    
    if len(appeals) == 0:
        return jsonify({
            "error": "bad_request", 
            "message": "appeal_id does not exist."
            }), 400

    decision = payload.get("decision")
    verdict = payload.get("verdict")
    notes = payload.get("notes")
    now = datetime.now(timezone.utc)

    if not notes:
        audit.log_appealed_decision(content_id, appeal_id, verdict, decision)
    else:
        audit.log_appealed_decision(content_id, appeal_id, verdict, decision, notes)

    time_taken = (now - datetime.fromisoformat(appeals[-1].get('timestamp'))).total_seconds()

    return jsonify({
        "content_id": content_id,
        "appeal_id": appeal_id,
        "verdict": verdict,
        "decision": decision,
        "confirmation": "Appeal decided.", 
        "time taken": time_taken
    }), 200

# ── Already works ─────────────────────────────────────────────────────────────

@app.get("/log")
def get_log():
    """
    The audit log, most recent last.

        curl "http://127.0.0.1:5000/log?limit=10"

    You need this in unit 8 to paste entries into your README, and you need it
    now to see whether your logging is actually working.
    """
    limit = request.args.get("limit", type=int)
    entries = audit.read_entries(limit=limit)
    return jsonify({"count": len(entries), "entries": entries})


def main():
    print(f"Provenance Guard on http://{config.HOST}:{config.PORT}")
    print(f"  detector model:  {config.DETECTOR_MODEL}")
    print(f"  rate limiting:   {'ON' if config.RATE_LIMITING_ENABLED else 'off (unit 8)'}")
    print(f"  audit log:       {config.AUDIT_LOG}")
    print()
    print("Check it's alive:")
    print(f'  curl -X POST http://{config.HOST}:{config.PORT}/ping \\')
    print('    -H "Content-Type: application/json" \\')
    print("    -d '{\"message\": \"hello\"}'")
    print()
    # debug=True hands out an interactive debugger, so it's local-only — see config.py
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)


if __name__ == "__main__":
    main()
