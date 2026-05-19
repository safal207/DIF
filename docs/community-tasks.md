# DIF Community Task Ladder

This document defines contributor-friendly tasks for DeepIntent Funnel (DIF), organized by difficulty.

The goal is to help different people contribute without needing to understand the entire project at once.

DIF should be easy to enter, but deep enough for serious contributors.

---

## Contribution Principle

DIF is not only a code project.

Useful contributions can be:

- examples;
- documentation;
- schemas;
- TypeScript types;
- scoring logic;
- CLI experiments;
- safety rules;
- product workflows;
- evaluation cases;
- UI prototypes;
- research notes.

A good contribution should make the path clearer:

```text
raw signal -> clarified intent -> action-ready output
```

---

## Difficulty Levels

| Level | Contributor type | Best task type |
|---|---|---|
| Level 1 | Newcomer | Fix wording, add simple examples |
| Level 2 | Beginner | Add structured examples or docs |
| Level 3 | Intermediate | Add schemas, types, small utilities |
| Level 4 | Advanced | Implement scoring and validation logic |
| Level 5 | Expert | Design evaluation, safety, and agent workflows |
| Level 6 | Professional | Build integrations, demos, and production-grade prototypes |

---

# Level 1 — Newcomer Tasks

These tasks are for people who want to help without deep technical knowledge.

## Task 1.1 — Improve README clarity

**Goal:** Make the README easier to understand for first-time visitors.

**Suggested work:**

- simplify long sentences;
- add one missing explanation;
- improve headings;
- make the 30-second example clearer.

**Definition of Done:**

- The README remains accurate.
- The main invariant is preserved.
- The project still leads with practical value.

**Suggested labels:**

```text
good first issue
documentation
beginner
```

---

## Task 1.2 — Add one more raw-signal example

**Goal:** Add a simple example of a messy human input.

**Example inputs:**

```text
I do not know what I want to build.
This customer message feels important but unclear.
The AI answer looks correct but not useful.
I have a drawing but cannot explain it.
```

**Suggested output:**

Add the example to an existing docs file or create a small file under:

```text
docs/examples/
```

**Definition of Done:**

- The example includes raw signal, possible meanings, human correction, and next action.
- The example does not claim final access to human intent.

---

## Task 1.3 — Add a glossary entry

**Goal:** Define one DIF term in simple language.

**Possible terms:**

- Signal;
- Meaning Hypothesis;
- Human Correction Loop;
- Confirmed Intent;
- Intent Graph;
- Decoherence Radar;
- Q-State Layer.

**Suggested file:**

```text
docs/glossary.md
```

**Definition of Done:**

- The term is explained in plain language.
- The explanation includes one short example.

---

# Level 2 — Beginner Tasks

These tasks require basic writing, product thinking, or light technical structure.

## Task 2.1 — Add an AI prompt clarification example

**Goal:** Show how DIF improves a vague AI prompt before generation.

**Raw signal:**

```text
Write me a landing page for my startup.
```

**Expected DIF flow:**

```text
Raw signal
-> visible signals
-> missing context
-> meaning hypotheses
-> human correction
-> confirmed intent
-> improved prompt or task brief
```

**Suggested file:**

```text
docs/examples/ai-prompt-clarification.md
```

**Definition of Done:**

- Includes at least 3 clarifying questions.
- Produces a better prompt or product brief.
- Includes a drift check.

---

## Task 2.2 — Add a product discovery example

**Goal:** Show how DIF helps a product manager clarify a messy feature request.

**Raw signal:**

```text
Users want more control over the dashboard.
```

**Expected output:**

- possible meanings;
- missing context;
- user segments;
- product risks;
- confirmed feature intent;
- one next discovery action.

**Suggested file:**

```text
docs/examples/product-discovery.md
```

---

## Task 2.3 — Create docs/glossary.md

**Goal:** Add a short glossary of core DIF terms.

**Required terms:**

- Signal;
- Context;
- Meaning Hypothesis;
- Correction;
- Confirmed Intent;
- Intent Graph;
- Action Output;
- Q-State Layer;
- Decoherence Radar.

**Definition of Done:**

- Each term has a plain-language definition.
- Each term has one tiny example.
- The glossary links back to the README where useful.

---

# Level 3 — Intermediate Tasks

These tasks require TypeScript, JSON Schema, or structured design.

## Task 3.1 — Add Q-State JSON schemas

**Goal:** Add JSON Schemas for the Q-State Layer.

**Suggested files:**

```text
schemas/q-state/intent-state-matrix.schema.json
schemas/q-state/partial-trace-view.schema.json
schemas/q-state/intent-channel.schema.json
schemas/q-state/decoherence-radar-result.schema.json
schemas/q-state/clarity-gain.schema.json
schemas/q-state/actionability-score.schema.json
```

**Definition of Done:**

- Schemas are valid JSON Schema.
- Scores use numbers from `0` to `1`.
- Schemas match `src/q-state/types.ts`.
- Each schema includes one example object.

---

## Task 3.2 — Add example JSON sessions

**Goal:** Convert the markdown examples into machine-readable session examples.

**Suggested files:**

```text
examples/sessions/startup-idea.session.json
examples/sessions/vague-ticket.session.json
examples/sessions/customer-complaint.session.json
```

**Definition of Done:**

- Each session includes signals, context, hypotheses, corrections, confirmed intents, graphs, and actions.
- The examples match existing core schemas.
- The examples remain small and readable.

---

## Task 3.3 — Add TypeScript sample data

**Goal:** Add sample DIF sessions as TypeScript objects.

**Suggested file:**

```text
src/examples/sessions.ts
```

**Definition of Done:**

- Uses existing types from `src/core/types.ts`.
- Includes at least one example session.
- No external dependencies.

---

# Level 4 — Advanced Tasks

These tasks require implementation design and careful semantics.

## Task 4.1 — Implement basic Decoherence Radar scoring

**Goal:** Implement a minimal scoring function for meaning drift.

**Suggested file:**

```text
src/q-state/decoherence.ts
```

**Suggested function:**

```ts
calculateDecoherenceRisk(input): DecoherenceRadarResult
```

**Inputs:**

- original signal text;
- confirmed intent text;
- current output text;
- constraints;
- corrections.

**Definition of Done:**

- Returns `DecoherenceRadarResult`.
- Produces low/medium/high risk.
- Includes clear reason text.
- No external dependencies for v0.1.
- Includes simple tests or examples.

---

## Task 4.2 — Implement Actionability Score

**Goal:** Estimate whether a confirmed intent is ready for action.

**Suggested file:**

```text
src/q-state/actionability.ts
```

**Checks:**

- goal clear;
- domain clear;
- constraints known;
- next action known;
- risks visible;
- human confirmed.

**Definition of Done:**

- Returns `ActionabilityScore`.
- Produces a recommendation.
- Handles incomplete intent gracefully.

---

## Task 4.3 — Add a lightweight CLI prototype

**Goal:** Create a simple CLI for running a DIF clarification session from a text file.

**Possible command:**

```bash
npx dif clarify examples/raw/vague-ticket.txt
```

**Expected output:**

```text
visible signals
meaning hypotheses
clarifying questions
suggested confirmed intent
next action
```

**Definition of Done:**

- CLI works locally.
- No heavy infrastructure.
- Uses existing types and examples.

---

# Level 5 — Expert Tasks

These tasks require research, safety thinking, or evaluation design.

## Task 5.1 — Design DIF evaluation cases

**Goal:** Create a benchmark-style set of cases to evaluate clarification quality.

**Suggested file:**

```text
docs/evaluation-cases.md
```

**Case categories:**

- vague product request;
- emotional support complaint;
- ambiguous AI prompt;
- conflicting user goals;
- high-impact decision;
- agent goal drift;
- rejected interpretation handling.

**Definition of Done:**

- At least 10 evaluation cases.
- Each case defines expected safe behavior.
- Each case defines failure modes.

---

## Task 5.2 — Define clarification quality metrics

**Goal:** Define how DIF can measure whether clarification improved the situation.

**Possible metrics:**

- ambiguity reduction;
- confirmed intent quality;
- actionability gain;
- drift risk;
- correction responsiveness;
- false certainty avoidance;
- missing context coverage.

**Suggested file:**

```text
docs/metrics.md
```

**Definition of Done:**

- Each metric has a definition.
- Each metric has a simple scoring method.
- Metrics connect to examples.

---

## Task 5.3 — Add high-impact domain safety rules

**Goal:** Extend DIF safety rules for health, finance, legal, family, and career decisions.

**Suggested file:**

```text
docs/high-impact-safety.md
```

**Definition of Done:**

- Defines what counts as high-impact.
- Defines when DIF should slow down.
- Defines when to recommend expert support.
- Preserves user agency.

---

# Level 6 — Professional Tasks

These tasks are for experienced builders who can turn DIF into working product surfaces.

## Task 6.1 — Build a web demo

**Goal:** Build a simple web UI that demonstrates DIF Task Clarifier.

**Suggested stack:**

- TypeScript;
- React or simple frontend;
- static examples first;
- no complex backend for v0.1.

**Demo flow:**

```text
paste vague request
-> see visible signals
-> answer clarification question
-> confirm intent
-> get task-ready output
-> see decoherence warning if scope drifts
```

**Definition of Done:**

- A user can complete one example flow.
- Demo uses existing examples.
- Demo does not overclaim intent understanding.

---

## Task 6.2 — Build GitHub Issue generator

**Goal:** Convert a confirmed intent into a GitHub-ready issue body.

**Suggested output:**

```text
Title
Problem
Context
Confirmed intent
Acceptance criteria
Risks
Next action
```

**Definition of Done:**

- Works on the vague-ticket example.
- Produces clean markdown.
- Makes missing context explicit.

---

## Task 6.3 — Build integration concept for AI agents

**Goal:** Define how DIF can sit before an AI agent executes a task.

**Suggested file:**

```text
docs/agent-integration.md
```

**Flow:**

```text
human goal
-> DIF clarification
-> confirmed intent
-> agent plan
-> decoherence check
-> tool execution
```

**Definition of Done:**

- Defines pre-execution gate.
- Defines drift check before tool use.
- Includes at least one example with an agent doing the wrong task if clarification is skipped.

---

# Maintainer Tasks

These are tasks for the core maintainer path.

## Maintainer Task A — Keep the project understandable

Before adding complexity, ask:

```text
Can a new visitor understand DIF in 60 seconds?
```

If not, improve examples before adding infrastructure.

---

## Maintainer Task B — Convert best tasks into GitHub Issues

Recommended first issues to open:

1. Add glossary.
2. Add AI prompt clarification example.
3. Add Q-State JSON schemas.
4. Implement basic Decoherence Radar scoring.
5. Design evaluation cases.
6. Build GitHub Issue generator.

---

## Maintainer Task C — Protect the core invariant

Every contribution should preserve:

```text
No system has final authority over human intention.
```

Pull requests should be checked for:

- false certainty;
- hidden manipulation;
- ignoring user correction;
- action before confirmation;
- overclaiming what DIF knows.

---

# Suggested Issue Template

```md
## Summary

Describe the task in 2-4 sentences.

## Difficulty

Level 1 / Level 2 / Level 3 / Level 4 / Level 5 / Level 6

## Suggested files

```text
path/to/file.md
```

## Why it matters

Explain how this improves DIF.

## Acceptance criteria

- [ ] Clear outcome exists.
- [ ] Main invariant is preserved.
- [ ] Example or test is included where useful.
- [ ] Contribution stays small enough to review.
```

---

# Priority Recommendation

The best next community-facing tasks are:

```text
1. docs/glossary.md
2. docs/examples/ai-prompt-clarification.md
3. schemas/q-state/*.schema.json
4. src/q-state/decoherence.ts
5. docs/evaluation-cases.md
```

This sequence moves DIF from clear concept to contributor-friendly implementation without jumping too early into heavy infrastructure.
