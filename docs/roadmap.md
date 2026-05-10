# DIF Roadmap v0.1

**From signal to intention.**

This roadmap defines the early path for DeepIntent Funnel (DIF): from concept clarity to a lightweight MVP and community contribution model.

DIF should not start with heavy infrastructure. The first win is the clarification loop.

## North Star

DIF helps people clarify what they are really trying to express, choose, create, change, or do before AI generates an answer.

```text
raw signal → context → meaning hypothesis → human correction → confirmed intent → graph → action
```

Main invariant:

> No system has final authority over human intention.

DIF can only propose, test, compare, version, and refine interpretations together with the human.

---

## Phase 0 — Concept Foundation

**Goal:** Make the idea understandable, precise, and safe.

### Outcomes

- Clear README.
- Project principles.
- Core terminology.
- Initial examples.
- Human-intent safety invariant.
- Public explanation of what DIF is and what it is not.

### Key Questions

- What is a raw signal?
- What is an intent?
- When is an intent confirmed enough?
- How does the system avoid pretending to understand the human?
- What should always stay under human control?

---

## Phase 1 — Method & Entities

**Goal:** Define the minimal conceptual model.

### Core Entities

- `Signal`
- `Context`
- `MeaningHypothesis`
- `Correction`
- `ConfirmedIntent`
- `IntentGraph`
- `ActionOutput`
- `Session`

### Outcomes

- Entity definitions.
- JSON examples.
- Simple schemas.
- Example clarification sessions.
- Versioned interpretation model.

### Success Criteria

A contributor should be able to read the docs and understand how DIF moves from a raw user input to a confirmed intent.

---

## Phase 2 — MVP Flow

**Goal:** Build a minimal working clarification loop.

### MVP Scope

Input types:

1. Text input.
2. Image description input.
3. Voice transcript input.

Output types:

1. Confirmed intent.
2. Meaning hypotheses.
3. Correction history.
4. Minimal intent graph.
5. One next action.

### MVP Flow

```text
1. User submits raw signal.
2. System asks 3–5 context questions.
3. System extracts visible signals.
4. System proposes 3 meaning hypotheses.
5. User corrects the interpretation.
6. System creates ConfirmedIntent v1.
7. System creates a small IntentGraph.
8. System suggests one ActionOutput.
```

### Success Criteria

The MVP should help a person clarify one real idea, decision, emotion, or project direction in less than 10 minutes.

---

## Phase 3 — Examples & Use Cases

**Goal:** Show DIF in real situations.

### Example Categories

- Startup idea clarification.
- Personal decision clarification.
- Project README generation.
- Drawing-to-intent session.
- Voice-thought-to-action session.
- “I don’t know what I want” session.
- Conflict or contradiction clarification.
- AI prompt clarification before generation.

### Success Criteria

A new visitor should understand the value of DIF through examples, not only through abstract explanation.

---

## Phase 4 — Lightweight Implementation

**Goal:** Create a simple usable prototype.

### Suggested Stack

- TypeScript.
- CLI or minimal web UI.
- Local JSON session storage.
- Optional LLM adapter.
- Schema-first entities.
- Exportable session record.

### Non-Goals

Do not start with:

- complex databases;
- multi-agent systems;
- heavy protocol design;
- distributed architecture;
- advanced memory infrastructure;
- enterprise features.

The first win is the clarification loop.

---

## Phase 5 — Community & Research Layer

**Goal:** Turn DIF into an open research and product-design project.

### Outcomes

- Contributing guide.
- Issue templates.
- Example sessions from contributors.
- Research questions.
- Evaluation criteria.
- Human-AI interaction notes.
- Safety principles around intent interpretation.

### Research Questions

- How can AI clarify intent without overclaiming understanding?
- How many correction loops are useful before the user feels friction?
- What makes an intent confirmed enough for action?
- How should conflicting interpretations be stored?
- Can intention clarification reduce wrong AI outputs?
- Can DIF become a pre-answer layer for AI agents and workflows?

---

## Version Plan

### v0.1 — Concept & Method

- README.
- Principles.
- Entities.
- MVP scope.
- Example sessions.
- Initial schemas.

### v0.2 — Session Model

- TypeScript entity types.
- Session object.
- Correction history.
- Confirmed intent versions.
- JSON export/import.

### v0.3 — CLI Prototype

- `dif clarify` command.
- Text-only clarification flow.
- Local session export.
- Example runs.

### v0.4 — Intent Graph

- Minimal graph model.
- Nodes and edges.
- Constraints, conflicts, causes, and actions.
- Graph export.

### v0.5 — Web Prototype

- Minimal web UI.
- Session view.
- Hypothesis selection.
- Correction loop.
- Intent graph preview.

### v1.0 — Usable DIF Alpha

- Stable clarification flow.
- Clear docs.
- Examples.
- Basic CLI or web UI.
- Safety rules.
- Evaluation criteria.
- Contributor guide.

---

## Final Reminder

DIF should not rush to answer.

DIF should first clarify the intention.

```text
Before the answer, clarify the intention.
```
