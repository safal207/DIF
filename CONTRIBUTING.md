# Contributing to DeepIntent Funnel (DIF)

Thank you for considering a contribution to DIF.

DIF is an early-stage open-source project about **intent clarification before AI or teams act**.

The core path is:

```text
raw signal -> meaning hypotheses -> human correction -> confirmed intent -> action-ready output
```

DIF needs contributors who can help make this path clearer through examples, documentation, schemas, types, prototypes, and evaluation cases.

If you are here for the first time, start with [First Steps](#first-steps).

---

## First Steps

1. Read the [`README.md`](README.md).
2. Skim the [`docs/community-tasks.md`](docs/community-tasks.md) task ladder.
3. Look for issues labeled `good first issue`, `beginner`, `examples`, or `documentation`.
4. Comment on an issue before starting work.
5. Open a small PR.

Useful links:

- [`README.md`](README.md) — project overview.
- [`docs/glossary.md`](docs/glossary.md) — core terms.
- [`docs/community-tasks.md`](docs/community-tasks.md) — tasks by difficulty.
- [`docs/examples/`](docs/examples/) — existing DIF examples.
- [`docs/contributor-invitation.md`](docs/contributor-invitation.md) — short invitation to share with potential contributors.

Suggested GitHub issue searches:

- `label:"good first issue"`
- `label:beginner`
- `label:examples`
- `label:documentation`

---

## Scope of DIF

DIF is an **intent clarification layer**.

It helps transform messy human input into:

- visible signals;
- missing context;
- meaning hypotheses;
- human correction;
- confirmed intent;
- action-ready output.

DIF should help people and teams avoid acting on vague prompts, unclear tickets, emotional complaints, and incomplete product requests.

Main invariant:

```text
No system has final authority over human intention.
```

DIF can propose, compare, test, and refine interpretations with the human.

DIF must not claim that it knows the user's true intent.

---

## Repository Boundaries

Please keep DIF focused.

Neighboring repositories have different roles:

```text
DIF -> intent clarification
DI  -> capabilities and limitations
DRP -> decision records and reasons
```

This means:

- if the contribution is about clarifying what a human means, it belongs in DIF;
- if it is about what is possible, impossible, risky, or bounded, it belongs closer to DI;
- if it is about recording what was decided and why, it belongs closer to DRP.

DIF should not become a broad productivity dashboard, task manager, or general decision-memory system.

---

## What DIF Is Not

DIF is not:

- a mind-reading system;
- a therapy replacement;
- a generic chatbot;
- a broad productivity dashboard;
- an autonomous decision maker;
- a system that claims final access to human intent.

Good framing:

```text
DIF clarifies human intent before AI or teams act.
```

Avoid over-hyped framing:

```text
AI that knows what people truly want.
```

---

## Types of Contributions

DIF is not only a code project.

Useful contributions can be documentation, examples, design, evaluation, schemas, or prototypes.

### Documentation and Examples

Good tasks:

- improve README clarity;
- add a new raw-signal example;
- improve existing examples;
- add glossary entries;
- clarify safety rules;
- write more realistic QA, support, product, or AI-prompt scenarios.

Example files:

```text
docs/examples/
docs/glossary.md
docs/safety.md
```

### Contributor Onboarding and UX

Good tasks:

- improve this `CONTRIBUTING.md`;
- improve [`docs/contributor-invitation.md`](docs/contributor-invitation.md);
- improve [`docs/community-tasks.md`](docs/community-tasks.md);
- suggest better issue labels;
- make the first contribution path clearer.

### DIF Logic and Architecture

Good tasks:

- improve TypeScript types;
- add JSON schemas;
- add machine-readable example sessions;
- define message structures between clarification stages;
- prototype small utilities that support intent clarification.

Keep architecture changes small and explain why they belong in DIF rather than DI or DRP.

### Research and Evaluation

Good tasks:

- design evaluation cases;
- define clarification quality metrics;
- document failure modes;
- test examples for false certainty or meaning drift;
- write research notes about intent clarification patterns.

---

## How to Choose a Task

Start from the [`docs/community-tasks.md`](docs/community-tasks.md) task ladder.

General guidance:

| Level | Good first direction |
|---|---|
| Level 1–2 | small docs, wording, glossary, examples |
| Level 3–4 | schemas, TypeScript samples, scoring prototypes |
| Level 5+ | evaluation, safety design, agent workflow research |

Ask yourself:

```text
Can this make the path from raw signal to clarified intent clearer?
```

If yes, it is probably useful for DIF.

Recommended first contributions:

- add one example;
- improve one existing example;
- add one glossary term;
- convert one example into machine-readable JSON;
- define one safety or evaluation case.

---

## How to Work on a Task

Recommended workflow:

1. Find an issue or task.
2. Comment on the issue, for example:

```text
I would like to work on this.
```

3. Ask clarifying questions if the task is ambiguous.
4. Fork the repository or create a branch.
5. Use a clear branch name:

```text
docs/<short-name>
examples/<short-name>
feat/<short-name>
fix/<short-name>
```

6. Open a draft PR if the work is larger than one small edit.
7. Keep the PR focused.

Avoid mixing unrelated changes in one PR.

---

## Pull Request Requirements

Use clear PR titles.

Recommended prefixes:

```text
docs: ...
examples: ...
types: ...
schemas: ...
feat: ...
fix: ...
```

A good PR should include:

- what changed;
- why it matters;
- which issue it relates to, if any;
- how to review or verify the change;
- any risks or limitations.

A good PR should also:

- preserve the main invariant;
- avoid overclaiming what DIF can know;
- include examples when adding a new concept;
- avoid mixing DIF with DI or DRP logic;
- stay small enough to review.

---

## How to Write a Good DIF Example

A good DIF example should include:

```text
Raw Signal
Visible Signals
Missing Context
Meaning Hypotheses
Human Correction
Confirmed Intent
Action Output
Decoherence / Drift Check
```

Example raw signals:

```text
The page is slow and users are unhappy.
Write me a landing page for my startup.
Users want more control over the dashboard.
Everything is broken. This is urgent.
```

The example should not pretend that the first interpretation is final.

It should show how a human can correct the system.

---

## Code Style and Project Conventions

DIF is still early.

The project currently focuses on:

- documentation;
- examples;
- TypeScript types;
- JSON schemas;
- small prototypes.

Until the implementation becomes heavier:

- prefer dependency-free examples;
- keep TypeScript types simple;
- keep schemas readable;
- add examples before adding complex infrastructure;
- avoid introducing large frameworks without a clear reason.

If you add behavior-changing code, include a small example or test where possible.

---

## Communication and Feedback

Use GitHub issues and PR comments for project discussion.

Good communication means:

- explain the motivation for changes;
- ask when intent is unclear;
- respect corrections;
- keep feedback specific and actionable;
- separate disagreement about ideas from judgment of people.

DIF is about clarification, so contributors should model that behavior in the project itself.

---

## Review Checklist

Before opening a PR, check:

- [ ] Does this improve intent clarification?
- [ ] Does it avoid claiming final access to human intent?
- [ ] Does it keep DIF separate from DI and DRP?
- [ ] Is the change small enough to review?
- [ ] Does it include a useful example or link to one?
- [ ] If behavior changes, is there a way to verify it?

---

## Start Right Now

To make your first contribution:

1. Read [`README.md`](README.md) and this file.
2. Pick a Level 1 or Level 2 task from [`docs/community-tasks.md`](docs/community-tasks.md).
3. Comment on the issue you want to work on.
4. Open a small PR, even if it only improves docs.

A clear example, a better definition, or a sharper safety rule can improve the project significantly.
