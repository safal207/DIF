# DeepIntent Funnel (DIF)

**From signal to intention.**

DeepIntent Funnel (DIF) is a human-AI communication system that helps transform raw human expression into clarified intention, structured meaning, and actionable direction.

DIF is not a chatbot, not prompt engineering, and not a mind map.

It is an intention clarification layer.

Most AI systems follow this pattern:

```text
user question → AI answer
```

DIF follows a deeper path:

```text
raw signal → context → meaning hypothesis → human correction → confirmed intent → decision → action
```

## Core Principle

DIF must never claim final access to human intention.

The system should not say:

> “I know what you mean.”

It should say:

> “I see these signals. One possible hypothesis of your intention is this. Confirm, correct, or reject it.”

## Why DIF Exists

People often cannot formulate the right request at the beginning.

The first prompt is not always the real intention.

DIF helps a person move from unclear inner signal to clarified intent before generating answers, plans, documents, prompts, or actions.

## Supported Raw Signals

DIF can start from:

- text;
- drawing;
- voice thought;
- emotion;
- screenshot;
- note;
- file;
- dialogue;
- word set;
- behavioral pattern in conversation.

## Funnel

```text
Raw Signal
  ↓
Context Capture
  ↓
Signal Extraction
  ↓
Meaning Hypotheses
  ↓
Human Correction Loop
  ↓
Intent Lock
  ↓
Intent Graph
  ↓
Action Output
```

## Main Invariant

**No system has final authority over human intention.**

DIF can only propose, test, compare, version, and refine interpretations together with the human.

## MVP v0.1

The first MVP should help a person:

1. submit a raw signal;
2. answer 3–5 context questions;
3. review several intent hypotheses;
4. correct the interpretation;
5. receive a confirmed intent;
6. get one concrete next action.

## Core Entities

- `Signal` — raw human expression.
- `Context` — situational frame.
- `MeaningHypothesis` — possible interpretation.
- `Correction` — user feedback on interpretation.
- `ConfirmedIntent` — human-confirmed direction.
- `IntentGraph` — structured map of meaning, causes, constraints, and actions.
- `ActionOutput` — concrete next step after clarification.
- `Session` — versioned clarification journey.

## Q-State Layer

DIF can also model intention as an uncertain evolving state.

The Q-State Layer introduces:

- `Intent State Matrix` — current map of possible meanings;
- `Partial Trace Views` — focused lenses on business, technical, emotional, or action context;
- `Intent Channels` — transitions caused by clarification, correction, and confirmation;
- `Decoherence Radar` — detection of meaning drift before AI or teams act.

This layer is quantum-inspired, not quantum computing. It exists to help DIF represent uncertainty, correction, and drift without claiming final authority over human intention.

See [`docs/q-state-layer.md`](docs/q-state-layer.md) and [`docs/decoherence-radar.md`](docs/decoherence-radar.md).

## Examples

DIF examples show the before/after transformation from messy input to clarified intent and action-ready output.

- [`docs/examples/startup-idea.md`](docs/examples/startup-idea.md) — startup idea → product direction.
- [`docs/examples/vague-ticket.md`](docs/examples/vague-ticket.md) — vague QA/support complaint → testable engineering ticket.
- [`docs/examples/customer-complaint.md`](docs/examples/customer-complaint.md) — emotional customer complaint → support triage action.

## Market Positioning

DIF's first practical wedge is:

```text
DIF helps teams clarify human intent before AI systems act.
```

The strongest early product direction is **DIF Task Clarifier**:

```text
vague request → clarified intent → structured task → AI / team action
```

See [`docs/market-positioning.md`](docs/market-positioning.md).

## Roadmap

See [`docs/roadmap.md`](docs/roadmap.md).

## Community Tasks

The first contributor-friendly tasks are tracked in GitHub Issues and documented in the roadmap.

Good first directions:

- improve examples;
- define entities;
- create schemas;
- design the clarification flow;
- build a lightweight TypeScript prototype;
- define safety and evaluation rules.

## Status

DIF is in early concept and architecture stage.

The current goal is to define the method, core entities, MVP flow, and examples before building heavy infrastructure.

## Slogans

- From signal to intention.
- Before the answer, clarify the intention.
- Not prompt engineering, but intention clarification.
- The first request is not always the real request.
- Не первый запрос важен, а намерение под ним.
- Не угадывать человека. Помочь человеку точнее услышать себя.
