# Contributing to DeepIntent Funnel (DIF)

Thank you for considering a contribution to DIF.

DIF is an early-stage open-source project about **intent clarification before AI or teams act**.

The core path is:

```text
raw signal -> meaning hypotheses -> human correction -> confirmed intent -> action-ready output
```

DIF needs contributors who can help make this path clearer through examples, documentation, schemas, types, prototypes, and evaluation cases.

## TL;DR

New here? Start small.

```text
Read README -> pick a small issue -> comment "I'd like to work on this" -> open a focused PR
```

Fast links:

- [How to choose a task](#how-to-choose-a-task)
- [How to work on a task](#how-to-work-on-a-task)
- [Pull request requirements](#pull-request-requirements)
- [Review checklist](#review-checklist)
- [Start right now](#start-right-now)

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
- `label:"help wanted"`

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

Good DIF contributions:

- add an example that clarifies a vague request;
- improve a clarification flow;
- make missing context more visible;
- reduce false certainty in docs or examples;
- add a safer way to handle human correction.

Not DIF contributions:

- general project management features;
- broad task tracking unrelated to intent clarification;
- decision-history logic that belongs in DRP;
- capability or limitation modeling that belongs in DI.

Main invariant:

```text
No system has final authority over human intention.
```

DIF can propose, compare, test, and refine interpretations with the human.

DIF must not claim that it knows the user's true intent.

---

## Repository Boundaries

Please keep DIF focused.

| Repository | Responsibility | Example contribution |
|---|---|---|
| DIF | examples and tools for intent clarification | clarify a vague ticket into confirmed intent |
| DI | capabilities and limitations | model what a system can or cannot do |
| DRP | decision records and reasons | record what was decided and why |

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

Start from one of two places:

1. GitHub issues labeled `good first issue`, `help wanted`, `documentation`, `examples`, or `beginner`.
2. The [`docs/community-tasks.md`](docs/community-tasks.md) task ladder.

Choose a task that is:

- small enough for 1–2 evenings;
- clearly scoped;
- aligned with DIF's focus on intent clarification;
- easy to review as one focused PR.

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

Before starting, comment on the issue:

```text
I'd like to work on this.
```

This helps avoid duplicate work.

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
2. Comment on the issue:

```text
I'd like to work on this.
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

6. Link the issue in the PR body.
7. Open a draft PR if the work is larger than one small edit.
8. Ask for review when the PR is ready.

Minimal workflow:

```text
Fork -> create branch -> make focused change -> link issue -> open PR -> ask for review
```

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

- linked issue, if one exists;
- clear summary of what changed;
- reason why the change matters;
- how to review or verify the change;
- updated docs, examples, or tests when applicable;
- risks or limitations, if relevant.

A good PR should also:

- preserve the main invariant;
- avoid overclaiming what DIF can know;
- include examples when adding a new concept;
- avoid mixing DIF with DI or DRP logic;
- stay small enough to review.

The [Review Checklist](#review-checklist) shows what maintainers look at when reviewing your PR.

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

Canonical examples:

- [`docs/examples/vague-ticket.md`](docs/examples/vague-ticket.md)
- [`docs/examples/ai-prompt-clarification.md`](docs/examples/ai-prompt-clarification.md)
- [`docs/examples/product-discovery.md`](docs/examples/product-discovery.md)

Example raw signals:

```text
The page is slow and users are unhappy.
Write me a landing page for my startup.
Users want more control over the dashboard.
Everything is broken. This is urgent.
```

Do:

- focus on clarifying intent under ambiguity;
- show at least one human correction;
- keep missing context explicit;
- include one concrete next action;
- include a drift or decoherence check.

Do not:

- treat the first interpretation as final;
- turn DIF into a general decision log;
- move capability or limitation modeling into DIF;
- invent requirements without marking them as assumptions;
- claim the system knows the user's true intent.

Mini-template:

```md
# Example: <Scenario Name>

## Raw Signal

## Visible Signals

## Missing Context

## Meaning Hypotheses

## Human Correction

## Confirmed Intent

## Action Output

## Decoherence / Drift Check
```

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

If you are unsure whether your idea fits DIF, open a short proposal issue before writing code.

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

1. Star the repository if the project is useful to you.
2. Read [`README.md`](README.md) and this file.
3. Pick a Level 1 or Level 2 task from [`docs/community-tasks.md`](docs/community-tasks.md), or choose one small docs improvement.
4. Comment on the issue you want to work on.
5. Open a small PR, even if it only improves docs.

Micro-task without deep context:

```text
Read the 30-second example in README and suggest one sentence that would make it clearer for a first-time visitor.
```

A clear example, a better definition, or a sharper safety rule can improve the project significantly.
