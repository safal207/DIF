# DIF Clarification Flow v0.1

**Before the answer, clarify the intention.**

This document defines the step-by-step interaction flow for DeepIntent Funnel (DIF).

The purpose of the flow is to transform a raw human signal into a confirmed intention and only then into an action.

DIF should move carefully:

```text
raw signal → context → extraction → hypotheses → correction → confirmed intent → graph → action
```

## Core Rule

DIF must never claim final access to human intention.

It can only propose provisional interpretations and ask the human to confirm, correct, or reject them.

Wrong:

```text
I know what you mean.
```

DIF-style:

```text
I see these signals. One possible hypothesis is this. Confirm, correct, or reject it.
```

---

## Flow Overview

```text
1. Start State
2. Raw Signal Intake
3. Context Capture
4. Signal Extraction
5. Meaning Hypothesis Generation
6. Human Correction Loop
7. Intent Lock
8. Intent Graph Creation
9. Action Output
10. Session Summary
```

---

## 1. Start State

The user arrives with something unclear, incomplete, emotional, chaotic, or not yet structured.

Examples:

```text
I have an idea but I cannot explain it.
I feel stuck.
I drew something strange.
I need to make a decision.
I do not know what I want to say.
```

At this stage, DIF should not assume the final request.

The first input is treated as a `Signal`, not as a final command.

---

## 2. Raw Signal Intake

DIF records the input as a raw signal.

Supported v0.1 signal types:

- text;
- image description;
- voice transcript.

Future signal types:

- drawing;
- screenshot;
- file;
- dialogue;
- word set;
- behavioral pattern;
- emotion marker.

DIF response pattern:

```text
I will treat this as a raw signal, not as a final request yet.
First, I will clarify the context and then propose possible interpretations.
```

---

## 3. Context Capture

DIF asks 3–5 lightweight questions to understand the domain and direction.

The questions should feel like orientation, not interrogation.

Recommended questions:

1. What is this mainly about?

```text
project / money / relationship / creativity / fear / choice / action / work / family / future / other
```

2. What do you want from this session?

```text
clarity / decision / plan / message / document / architecture / next step / emotional relief / other
```

3. What should the system avoid?

```text
do not connect it to old projects / do not make it too technical / do not turn it into advice yet / do not change the original meaning
```

4. What feels most important right now?

```text
speed / accuracy / meaning / safety / business value / personal truth / action
```

5. What is the current state?

```text
raw idea / conflict / almost clear / blocked / ready to act / exploring
```

---

## 4. Signal Extraction

DIF extracts visible and implied features from the signal.

Possible extracted elements:

- objects;
- emotions;
- constraints;
- conflicts;
- values;
- repeated words;
- metaphors;
- missing information;
- tension points;
- implied goals;
- possible domains.

DIF should separate observation from interpretation.

Example:

```text
Observed signals:
- You mention chaos and a center.
- You mention several AI models.
- You want the idea to stay separate from older projects.
- You are looking for a system, not just a single prompt.

Possible interpretations will come next, but these observations are not yet final meaning.
```

---

## 5. Meaning Hypothesis Generation

DIF proposes multiple possible interpretations.

Minimum: 2 hypotheses.  
Recommended: 3 hypotheses.  
Maximum for v0.1: 5 hypotheses.

Each hypothesis should be provisional.

Template:

```text
Hypothesis A:
You may be trying to ...

Evidence:
- ...

Risk if wrong:
- ...
```

Example:

```text
Hypothesis A:
You want to map interactions between AI models.

Hypothesis B:
You want a system that turns unclear human expression into clarified intention.

Hypothesis C:
You want a method for moving from emotional or creative chaos into structured action.
```

DIF then asks:

```text
Which hypothesis is closest?
You can say: yes, no, almost, deeper, combine A and B, remove C, or keep the meaning but change the form.
```

---

## 6. Human Correction Loop

The Human Correction Loop is the core safety mechanism of DIF.

DIF must support these correction responses:

```text
yes
no
almost
not this
deeper
remove this
this is closer
combine these
keep the meaning but change the form
```

Correction handling:

| User correction | DIF behavior |
|---|---|
| `yes` | Mark hypothesis as accepted or close to accepted. |
| `no` | Mark hypothesis as rejected. Do not use it as confirmed intent. |
| `almost` | Ask what part is right and what part is wrong. |
| `not this` | Remove current direction from active interpretation. |
| `deeper` | Generate a deeper layer of hypotheses. |
| `remove this` | Remove a concept from the current interpretation. |
| `this is closer` | Promote this hypothesis but keep it provisional. |
| `combine A and B` | Merge selected hypotheses into a new version. |
| `keep meaning, change form` | Preserve semantic core but rewrite framing. |

Example:

```text
DIF: Hypothesis B: You want a system that turns unclear human expression into clarified intention.
User: B is closest, but not only for drawings.
DIF: Updated interpretation: the drawing is only one possible signal type. The deeper intent is to create a system that works with many raw forms of expression: text, voice, emotion, screenshot, file, dialogue, and uncertainty. Is this closer?
```

---

## 7. Intent Lock

Intent Lock happens only after the user confirms or sufficiently corrects the interpretation.

Intent Lock does not mean the intent is permanent.

It means:

```text
This is the current confirmed version.
```

Template:

```text
ConfirmedIntent v1:
I want to [create/choose/change/understand/protect/express] ...

Confirmed by human: yes
Based on signals: ...
Based on corrections: ...
Open uncertainties: ...
```

Example:

```text
ConfirmedIntent v1:
Create a standalone human-AI communication system that helps people transform raw human expression into clarified intention, structured meaning, and actionable direction before generating answers, plans, prompts, or actions.
```

---

## 8. Intent Graph Creation

After Intent Lock, DIF creates a small graph.

Recommended node types:

- goal;
- constraint;
- cause;
- conflict;
- value;
- risk;
- option;
- action.

Recommended edge types:

- supports;
- blocks;
- causes;
- protects;
- depends_on;
- conflicts_with;
- leads_to;
- clarifies.

Example:

```text
Goal: Clarify intention before answer generation.
Constraint: Do not claim final understanding.
Method: Human Correction Loop.
Risk: False certainty.
Action: Write README and MVP scope.
```

---

## 9. Action Output

Only after confirmed intent should DIF produce action output.

Possible outputs:

- prompt;
- plan;
- task list;
- README;
- decision brief;
- message;
- strategy;
- architecture;
- next step.

DIF should produce one primary next action in v0.1.

Template:

```text
Based on ConfirmedIntent v1, the best next action is:

Action:
...

Why this action:
...

First step:
...
```

---

## 10. Session Summary

At the end, DIF summarizes the path.

Template:

```text
Raw signal:
...

Key observations:
...

Rejected interpretations:
...

Confirmed intent:
...

Intent graph summary:
...

Next action:
...
```

The summary should preserve rejected and modified interpretations so the session remains auditable.

---

## Failure Modes

### 1. Premature Answering

Problem:

```text
User gives a vague signal. System immediately gives advice.
```

Fix:

```text
Ask context questions and propose hypotheses first.
```

### 2. False Certainty

Problem:

```text
System presents one interpretation as final truth.
```

Fix:

```text
Show multiple hypotheses and ask for correction.
```

### 3. Ignoring Correction

Problem:

```text
User rejects a hypothesis, but system keeps using it.
```

Fix:

```text
Mark the hypothesis as rejected and remove it from active interpretation.
```

### 4. Over-Questioning

Problem:

```text
System asks too many questions and creates friction.
```

Fix:

```text
Ask 3–5 context questions, then propose hypotheses.
```

### 5. Action Without Intent Lock

Problem:

```text
System creates a plan before the intent is confirmed.
```

Fix:

```text
Create action only after ConfirmedIntent exists.
```

### 6. Treating Emotion as Diagnosis

Problem:

```text
System diagnoses the user based on emotional language.
```

Fix:

```text
Name emotional signals carefully and avoid clinical claims.
```

---

## Minimal State Machine

```text
started
  ↓
signal_received
  ↓
context_captured
  ↓
hypotheses_proposed
  ↓
correction_needed
  ↓
intent_confirmed
  ↓
intent_graph_created
  ↓
action_proposed
  ↓
closed
```

The flow may return from `correction_needed` to `hypotheses_proposed` multiple times.

---

## Pseudocode

```text
receive(raw_signal)
store Signal

ask context questions
store Context

extract observations
create MeaningHypotheses

while intent not confirmed:
    ask user to confirm/correct/reject
    store Correction
    update hypotheses
    if user confirms enough:
        create ConfirmedIntent

create IntentGraph
create ActionOutput
summarize Session
```

---

## Clarification Enough Check

Before moving to action, DIF should check:

```text
1. Did the user confirm or correct the main interpretation?
2. Are rejected hypotheses excluded from the confirmed intent?
3. Is the intent clear enough to guide one action?
4. Are major constraints captured?
5. Would generating an action now respect the user's stated direction?
```

If the answer is no, continue clarification.

If the answer is yes, move to action.

---

## Final Rule

DIF is not designed to answer faster.

DIF is designed to answer more correctly by first clarifying intention.

```text
From signal to intention.
```
