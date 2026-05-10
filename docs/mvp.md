# DIF MVP v0.1

The first MVP of DeepIntent Funnel should prove one thing:

> A person can start with an unclear signal and leave with a clearer confirmed intention and one useful next action.

No heavy infrastructure is needed for v0.1.

---

## Target User

A person who has a raw or unclear inner signal:

- an idea they cannot explain yet;
- a project direction;
- a decision;
- a conflict;
- a voice thought;
- a drawing;
- an emotional signal;
- a vague question;
- a need to create something but no clear brief.

---

## Main Use Case

```text
I have something in my head, but I cannot formulate it clearly yet.
```

DIF helps transform this into:

```text
ConfirmedIntent v1 + IntentGraph + one next action
```

---

## Input Types

For v0.1, support only three input types:

1. Text input.
2. Image description input.
3. Voice transcript input.

Image processing can start as user-provided description. Direct image analysis can come later.

---

## Output Types

For v0.1, produce only five outputs:

1. Clarified intent.
2. Meaning hypotheses.
3. Correction history.
4. Minimal intent graph.
5. One next action.

---

## MVP Flow

```text
1. User submits raw signal.
2. DIF asks 3–5 context questions.
3. DIF extracts visible signals.
4. DIF proposes 3 meaning hypotheses.
5. User corrects the interpretation.
6. DIF creates ConfirmedIntent v1.
7. DIF creates a small IntentGraph.
8. DIF suggests one ActionOutput.
```

---

## Minimal Product Behavior

### Step 1 — Raw Signal Intake

User enters something unclear:

```text
I drew a strange map with AI models, lines, chaos, and a center. I feel there is a project here.
```

### Step 2 — Context Capture

DIF asks:

```text
Is this mainly about a project, decision, emotion, relationship, business idea, or creative direction?
```

### Step 3 — Signal Extraction

DIF identifies:

- central organizing point;
- multiple AI models;
- movement from chaos to structure;
- need to turn a visual idea into a system;
- possible communication funnel.

### Step 4 — Meaning Hypotheses

DIF proposes:

```text
A. You want to map interactions between AI models.
B. You want a system that turns unclear human expression into clear intention.
C. You want a method for moving from emotional chaos to structured action.
```

### Step 5 — Human Correction

User says:

```text
B is closest, but it should work not only for drawings.
```

### Step 6 — Intent Lock

DIF creates:

```text
ConfirmedIntent v1:
Create a standalone system that helps people transform raw expression into clarified intention before generating answers, plans, or actions.
```

### Step 7 — Intent Graph

DIF creates a small graph:

```text
Goal: clarify intention
Constraint: do not claim final understanding
Method: human correction loop
Output: action after intent lock
```

### Step 8 — Action Output

DIF suggests:

```text
Next action: write README and define MVP v0.1.
```

---

## Non-Goals for v0.1

Do not build yet:

- distributed memory;
- complex databases;
- autonomous agents;
- enterprise workflows;
- multi-user collaboration;
- long-term personal memory;
- heavy protocol specifications;
- clinical or therapeutic features.

---

## Success Criteria

The MVP is useful if:

1. A user can clarify one raw signal in less than 10 minutes.
2. The system produces at least 2–3 alternative hypotheses before action.
3. The user can correct or reject interpretations.
4. The final intent is clearly versioned.
5. The final action follows from the confirmed intent.
6. The system avoids claiming final access to the user's intention.

---

## First Implementation Direction

Recommended stack:

- TypeScript;
- CLI first or minimal web UI;
- local JSON session storage;
- schema-first entities;
- optional LLM adapter;
- exportable session file.

The first implementation should feel more like a clear thinking instrument than a chatbot.
