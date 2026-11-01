# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

<!-- Your criterion. It must name a number. -->

Only 1 in 10 writing samples may be a false positive.

**Why this target:**

Being falsely accused of not writing your own work is the most harmful thing that can happen to a writer in this system. I only allow one false positive for truly in the middle cases. 

---

## 2.

<!-- Your criterion. -->

Every appeal is recorded in the audit log and correctly flagged as `under_review`.

**Why this target:**

Every appeal should be noted correctly in the `audit_log` to be followed up on later and not lost in the system. It shouldn't be on the user to chase after their appeal and making sure it got looked at. Therefore, appeals should always be noted correctly in the audit log so they can be processed correctly.

---

## 3.

<!-- Your criterion. -->

The model correctly identifies at least one of each label (human, unclear, AI).

**Why this target:**

The model/decision making must be able to reach each label at least once, indicating that it is capable of doing so. If no text is marked as AI generated despite one of them clearly being so, that tells us there is a failure on some part of the pipeline, and so on with the other labels.

---

## 4.

<!-- Your criterion. -->

Every might-be/might-not-be text is labeled correctly as such. 

**Why this target:**

Like people, the model/system should know that an "I don't know" answer is equally better than a random guess in either direction, especially when the decision impacts user's trust. If the model is unclear, it should clearly state so, rather than risk a decision in the wrong direction.

---

## 5.

<!-- Your criterion. -->

All clearly-AI and clearly-human text should score at least 0.25 apart. 

**Why this target:**

There should be a clear distinction in scoring between the ends of the scoring and labeling spectrum. If the midpoint is 0.50, 0.25 allows for 0.125 on either side, which allows for the unsure labels to live between 0.375 and 0.625. 

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
