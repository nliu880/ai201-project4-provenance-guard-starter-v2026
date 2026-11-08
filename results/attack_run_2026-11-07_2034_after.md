# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-07 20:34
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c_c477f459f394` | human | 0.367 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c_29ac1f378aa5` | unsure | 0.600 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c_7bf6ca78963d` | ai | 0.669 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c_d4133aa01613` | ai | 0.676 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c_35105f9b9689` | unsure | 0.395 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c_e4bc59722b80` | unsure | 0.427 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c_1fce7b9d2a84` | ai | 0.669 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `c_d017dc8600b0` | unsure | 0.436 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c_78b1a87ec8b8` | ai | 0.634 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c_949dc832c59b` | ai | 0.798 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c_697fa2fbf371` | unsure | 0.601 | BROKE |
| FP02 | false_positive | human writing in a formal register | 200 | `c_3162052cd98f` | ai | 0.720 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c_b39b03dfa00e` | ai | 0.752 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c_e411778e1447` | ai | 0.766 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `c_fc551cb19129` | ai | 0.744 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `c_63137f4a095f` | ai | 0.783 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c_6e134e538c08` | ai | 0.769 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `c_6a2c08fb18e3` | unsure | 0.502 | BROKE |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c_5b9781ceabcf` | unsure | 0.525 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c_35e6911a1339` | human | 0.314 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c_293195516160` | unsure | 0.538 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c_7d4cabaaff4c` | unsure | 0.553 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c_ff4058909025` | ai | 0.658 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c_1a81b700d08a` | unsure | 0.547 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | `—` | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — | HELD |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_338f87b48751` | human | 0.306 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_99c7530f0672` | human | 0.306 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_2364a98bb134` | human | 0.306 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_047ed1cba088` | human | 0.306 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_ac2386fe9cdf` | human | 0.306 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "c_c477f459f394",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3668948599774668,
  "model_score": 0.1635,
  "style_score": 0.7446281713641908,
  "label": "We believe this text was written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "c_29ac1f378aa5",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5997201720093324,
  "model_score": 0.5943,
  "style_score": 0.6051403440186647,
  "label": "We aren't sure whether this text was written by a person or generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c_7bf6ca78963d",
  "creator_id": "attacker_EV03",
  "guess": "ai",
  "confidence": 0.6691797143206255,
  "model_score": 0.6662,
  "style_score": 0.6721594286412511,
  "label": "We believe this text was generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "c_d4133aa01613",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.6758415656671444,
  "model_score": 0.6114,
  "style_score": 0.7402831313342887,
  "label": "We believe this text was generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "c_35105f9b9689",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.39486772747869886,
  "model_score": 0.3212,
  "style_score": 0.5316792213677111,
  "label": "We aren't sure whether this text was written by a person or generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "c_e4bc59722b80",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4268349888043035,
  "model_score": 0.5727,
  "style_score": 0.15594282515515284,
  "label": "We aren't sure whether this text was written by a person or generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "c_1fce7b9d2a84",
  "creator_id": "attacker_EV07",
  "guess": "ai",
  "confidence": 0.6689681443298969,
  "model_score": 0.5862,
  "style_score": 0.822680412371134,
  "label": "We believe this text was generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "c_d017dc8600b0",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4360558838609295,
  "model_score": 0.2452,
  "style_score": 0.7905025253169417,
  "label": "We aren't sure whether this text was written by a person or generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "c_78b1a87ec8b8",
  "creator_id": "attacker_EV09",
  "guess": "ai",
  "confidence": 0.63379953675609,
  "model_score": 0.6505,
  "style_score": 0.61709907351218,
  "label": "We believe this text was generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c_949dc832c59b",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.798176220998866,
  "model_score": 0.9744,
  "style_score": 0.4709034885681884,
  "label": "We believe this text was generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "c_697fa2fbf371",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.600814200878038,
  "model_score": 0.6175,
  "style_score": 0.584128401756076,
  "label": "We aren't sure whether this text was written by a person or generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "c_3162052cd98f",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7197362690495465,
  "model_score": 0.7387,
  "style_score": 0.7007725380990929,
  "label": "We believe this text was generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c_b39b03dfa00e",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7518503846255417,
  "model_score": 0.8051,
  "style_score": 0.6529582417872617,
  "label": "We believe this text was generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "c_e411778e1447",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7655829100150566,
  "model_score": 0.8329,
  "style_score": 0.6982658200301134,
  "label": "We believe this text was generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "c_fc551cb19129",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.743937551275835,
  "model_score": 0.8005,
  "style_score": 0.68737510255167,
  "label": "We believe this text was generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "c_63137f4a095f",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.783431946786169,
  "model_score": 0.8814,
  "style_score": 0.6014912765319116,
  "label": "We believe this text was generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "c_6e134e538c08",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7692681731311891,
  "model_score": 0.8816,
  "style_score": 0.5606519232319687,
  "label": "We believe this text was generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "c_6a2c08fb18e3",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.5015999184048541,
  "model_score": 0.3223,
  "style_score": 0.8345854811567261,
  "label": "We aren't sure whether this text was written by a person or generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "c_5b9781ceabcf",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.5251880536094775,
  "model_score": 0.4625,
  "style_score": 0.6416087245985072,
  "label": "We aren't sure whether this text was written by a person or generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "c_35e6911a1339",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.3140715467371453,
  "model_score": 0.1278,
  "style_score": 0.6600044192489867,
  "label": "We believe this text was written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "c_293195516160",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.537929138293426,
  "model_score": 0.4769,
  "style_score": 0.6512689665526459,
  "label": "We aren't sure whether this text was written by a person or generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "c_7d4cabaaff4c",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5532036547829603,
  "model_score": 0.4998,
  "style_score": 0.6523818708084579,
  "label": "We aren't sure whether this text was written by a person or generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "c_ff4058909025",
  "creator_id": "attacker_PI05",
  "guess": "ai",
  "confidence": 0.6579729799590208,
  "model_score": 0.6401,
  "style_score": 0.6758459599180417,
  "label": "We believe this text was generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "c_1a81b700d08a",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5473112999053837,
  "model_score": 0.5001,
  "style_score": 0.5945225998107676,
  "label": "We aren't sure whether this text was written by a person or generated by an AI model.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "c_338f87b48751",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3064327777777777,
  "model_score": 0.0287,
  "style_score": 0.8222222222222222,
  "label": "We believe this text was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "c_99c7530f0672",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3064327777777777,
  "model_score": 0.0287,
  "style_score": 0.8222222222222222,
  "label": "We believe this text was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "c_2364a98bb134",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3064327777777777,
  "model_score": 0.0287,
  "style_score": 0.8222222222222222,
  "label": "We believe this text was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "c_047ed1cba088",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3064327777777777,
  "model_score": 0.0287,
  "style_score": 0.8222222222222222,
  "label": "We believe this text was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "c_ac2386fe9cdf",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3064327777777777,
  "model_score": 0.0287,
  "style_score": 0.8222222222222222,
  "label": "We believe this text was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
