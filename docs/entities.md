# DIF Core Entities

This document defines the minimal conceptual entities for DeepIntent Funnel (DIF) v0.1.

The goal is to keep the model simple enough for early implementation while preserving the core meaning of the project.

---

## Signal

A `Signal` is raw human expression before it becomes clear.

Examples:

- text;
- drawing;
- voice transcript;
- emotion;
- screenshot;
- file;
- dialogue fragment;
- word set;
- behavioral pattern in conversation.

Purpose:

The signal is the starting point of the funnel.

Basic fields:

```json
{
  "id": "signal_001",
  "type": "text",
  "content": "I have an idea but I cannot explain it yet.",
  "createdAt": "2026-05-10T12:00:00Z"
}
```

---

## Context

A `Context` is the situational frame around a signal.

Examples:

- project context;
- emotional context;
- business context;
- relationship context;
- family context;
- creative context;
- decision context.

Purpose:

Context helps DIF avoid interpreting the signal in the wrong domain.

Basic fields:

```json
{
  "domain": "project",
  "userGoal": "turn unclear idea into a project concept",
  "constraints": ["keep it separate from other projects"],
  "timeframe": "early concept stage"
}
```

---

## MeaningHypothesis

A `MeaningHypothesis` is a possible interpretation of the signal.

It is not final. It must be confirmed, corrected, or rejected by the human.

Purpose:

Meaning hypotheses let the system show multiple possible readings instead of pretending certainty.

Basic fields:

```json
{
  "id": "hypothesis_001",
  "text": "You may be trying to turn a chaotic inner signal into a structured project direction.",
  "confidence": "medium",
  "evidence": ["chaos", "central idea", "need for structure"],
  "status": "proposed"
}
```

---

## Correction

A `Correction` is human feedback on an interpretation.

Examples:

```text
yes
no
almost
deeper
not this
remove this
this is close
keep the meaning but change the form
```

Purpose:

Correction is the central safety mechanism of DIF.

Basic fields:

```json
{
  "id": "correction_001",
  "targetHypothesisId": "hypothesis_001",
  "feedback": "close, but not only for drawings",
  "effect": "modify",
  "createdAt": "2026-05-10T12:05:00Z"
}
```

---

## ConfirmedIntent

A `ConfirmedIntent` is the current human-confirmed version of intention.

It is not eternal. It is versioned.

Purpose:

Confirmed intent defines what the system is allowed to act on.

Basic fields:

```json
{
  "id": "intent_001",
  "version": 1,
  "statement": "Create a standalone system that helps people transform raw expression into clarified intention before generating answers or actions.",
  "confirmedByHuman": true,
  "sourceSignalIds": ["signal_001"],
  "createdAt": "2026-05-10T12:10:00Z"
}
```

---

## IntentGraph

An `IntentGraph` is a structured map of the confirmed intent.

It may include:

- goals;
- causes;
- constraints;
- conflicts;
- values;
- risks;
- options;
- next actions.

Purpose:

The graph turns a confirmed intent into a navigable structure.

Basic fields:

```json
{
  "nodes": [
    { "id": "goal_001", "type": "goal", "label": "Clarify human intention" },
    { "id": "constraint_001", "type": "constraint", "label": "Do not claim final understanding" }
  ],
  "edges": [
    { "from": "constraint_001", "to": "goal_001", "type": "protects" }
  ]
}
```

---

## ActionOutput

An `ActionOutput` is a concrete next step generated after clarification.

Examples:

- write a README;
- create a project brief;
- generate a prompt;
- create a task list;
- send a message;
- choose between options;
- define an MVP.

Purpose:

ActionOutput bridges clarified intent into action.

Basic fields:

```json
{
  "id": "action_001",
  "type": "document",
  "title": "Write DIF README v0.1",
  "description": "Create a clear README explaining the concept, invariant, funnel, and MVP.",
  "dependsOnIntentId": "intent_001"
}
```

---

## Session

A `Session` is the full clarification journey.

It contains raw signals, context, hypotheses, corrections, confirmed intents, graph states, and action outputs.

Purpose:

Session preserves the versioned path from signal to intention.

Basic fields:

```json
{
  "id": "session_001",
  "signals": [],
  "context": {},
  "hypotheses": [],
  "corrections": [],
  "confirmedIntents": [],
  "intentGraphs": [],
  "actions": [],
  "status": "intent_confirmed"
}
```

---

## Entity Flow

```text
Signal
  ↓
Context
  ↓
MeaningHypothesis
  ↓
Correction
  ↓
ConfirmedIntent
  ↓
IntentGraph
  ↓
ActionOutput
```

The human correction loop may repeat several times before ConfirmedIntent is created.
