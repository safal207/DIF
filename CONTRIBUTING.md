# Contributing to DeepIntent Funnel (DIF)

Thank you for considering a contribution to DIF.

DIF is an early-stage open-source project about **intent clarification before AI or teams act**.

The core idea:

```text
raw signal -> meaning hypotheses -> human correction -> confirmed intent -> action-ready output
```

DIF should help people and teams avoid acting on vague prompts, unclear tickets, emotional complaints, and incomplete product requests.

---

## What DIF Is

DIF is an intention clarification layer.

It helps transform messy human input into:

- visible signals;
- missing context;
- meaning hypotheses;
- human correction;
- confirmed intent;
- structured tasks, prompts, tickets, or briefs.

---

## What DIF Is Not

DIF is not:

- a mind-reading system;
- a therapy replacement;
- a generic chatbot;
- a broad productivity dashboard;
- an autonomous decision maker;
- a system that claims final access to human intent.

Main invariant:

```text
No system has final authority over human intention.
```

---

## Good First Contributions

You do not need to understand the whole project to contribute.

Good first contributions include:

- improving README clarity;
- adding simple examples;
- improving the glossary;
- adding clarification questions;
- adding documentation links;
- fixing wording or structure;
- turning vague scenarios into DIF examples.

Start here:

- [`docs/community-tasks.md`](docs/community-tasks.md)
- GitHub issues labeled `good first issue`, `beginner`, or `examples`

---

## Contribution Levels

DIF welcomes contributions at different levels.

| Level | Good contribution type |
|---|---|
| Newcomer | Wording, examples, glossary entries |
| Beginner | Structured docs and clarification examples |
| Intermediate | JSON schemas, TypeScript examples, sample sessions |
| Advanced | Scoring logic, validation, CLI experiments |
| Expert | Evaluation, safety rules, agent workflows |
| Professional | Demos, integrations, product prototypes |

---

## How to Choose a Task

Ask yourself:

```text
Can this make the path from raw signal to clarified intent clearer?
```

If yes, it is probably useful.

Recommended first issues:

- add an example;
- improve one existing example;
- add a glossary term;
- convert an example into machine-readable JSON;
- define one safety or evaluation case.

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

---

## Pull Request Guidelines

Keep PRs small and reviewable.

A good PR should:

- explain what it changes;
- link to an issue when possible;
- preserve the main invariant;
- avoid overclaiming what DIF can know;
- include examples when adding a new concept;
- avoid mixing DIF with neighboring repositories like DI or DRP.

Repository boundaries:

```text
DIF -> intent clarification
DI  -> capabilities and limitations
DRP -> decision records and reasons
```

---

## Review Checklist

Before opening a PR, check:

- [ ] Does this improve intent clarification?
- [ ] Does it avoid claiming final access to human intent?
- [ ] Does it keep DIF separate from DI and DRP?
- [ ] Is the change small enough to review?
- [ ] Does it include a useful example or link to one?

---

## Tone and Style

Prefer clear and practical language.

Good framing:

```text
DIF clarifies human intent before AI or teams act.
```

Avoid over-hyped framing:

```text
AI that knows what people truly want.
```

DIF should sound practical, careful, and useful.

---

## Development Notes

The project currently focuses on:

- documentation;
- examples;
- TypeScript types;
- schemas;
- small prototypes.

Avoid heavy infrastructure until the core method is clearer.

---

## Thank You

DIF is early.

A helpful contribution is not only code.

A clear example, a better definition, or a sharper safety rule can improve the project significantly.
