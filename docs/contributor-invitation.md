# Contributor Invitation

DeepIntent Funnel (DIF) is looking for early contributors.

DIF explores a simple problem:

```text
AI and teams often act before human intent is clear.
```

The project goal:

```text
clarify human intent before AI or teams act
```

---

## Why This Matters

Many failures start before execution:

- vague prompts;
- unclear tickets;
- emotional customer complaints;
- broad product requests;
- missing context;
- hidden assumptions;
- scope drift.

DIF helps turn messy input into:

```text
visible signals -> meaning hypotheses -> human correction -> confirmed intent -> action-ready output
```

---

## Example

Raw signal:

```text
The page is slow and users are unhappy.
```

DIF-style clarification:

```text
What page?
Which users?
What does slow mean?
When did it start?
Is it frontend, API, websocket, cache, or data loading?
What is expected vs actual behavior?
```

Action-ready output:

```text
A testable engineering ticket with reproduction steps, missing context, acceptance criteria, and a drift check.
```

---

## Who Can Help

You may be a good fit if you are:

- a QA engineer;
- a product manager;
- a support lead;
- an AI builder;
- a TypeScript developer;
- a UX researcher;
- a safety/evaluation researcher;
- someone tired of vague tasks and bad AI outputs.

---

## Good First Contributions

You can help by:

- improving examples;
- adding new raw-signal scenarios;
- improving glossary definitions;
- adding JSON schemas;
- creating machine-readable sessions;
- designing evaluation cases;
- prototyping a GitHub issue generator;
- reviewing whether the README is understandable in 30 seconds.

Start here:

- [`CONTRIBUTING.md`](../CONTRIBUTING.md)
- [`docs/community-tasks.md`](community-tasks.md)
- [`docs/examples/`](examples/)

---

## First Feedback Request

If you only have 5 minutes, answer one question:

```text
Does the README explain DIF clearly in 30 seconds?
```

If not, open an issue or PR with what confused you.

---

## Project Boundary

DIF is focused on intent clarification.

Neighboring repositories have different roles:

```text
DIF -> intent clarification
DI  -> capabilities and limitations
DRP -> decision records and reasons
```

Please keep DIF contributions focused on intent clarification.
