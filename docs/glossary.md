# DIF Glossary

This glossary explains the core terms used in DeepIntent Funnel (DIF).

The goal is to make DIF easier to understand for new contributors, users, and reviewers.

Core principle:

```text
No system has final authority over human intention.
```

DIF can only propose, test, compare, version, and refine interpretations together with the human.

---

## Signal

A `Signal` is raw human expression before it becomes clear intent.

A signal can be text, a drawing, a voice transcript, a screenshot, a file, an emotional phrase, a dialogue fragment, or a vague request.

Example:

```text
The page is slow and users are unhappy.
```

This is not yet a final task. It is the starting signal.

See: [`docs/entities.md`](entities.md)

---

## Context

`Context` is the situational frame around a signal.

It helps DIF avoid interpreting the same signal in the wrong domain.

Example:

```text
The signal is about a production trading dashboard used by customers during market switching.
```

Without context, DIF may confuse a performance issue with a design request.

See: [`docs/entities.md`](entities.md)

---

## Meaning Hypothesis

A `Meaning Hypothesis` is a possible interpretation of a signal.

It is provisional. It must be confirmed, corrected, or rejected by the human.

Example:

```text
The user may be reporting a frontend performance issue.
```

Another possible hypothesis:

```text
The user may be reporting delayed websocket updates.
```

DIF should show multiple hypotheses instead of pretending certainty.

See: [`docs/clarification-flow.md`](clarification-flow.md)

---

## Human Correction Loop

The `Human Correction Loop` is the process where the human confirms, rejects, modifies, or deepens DIF's interpretation.

Supported corrections include:

```text
yes
no
almost
not this
deeper
remove this
this is closer
keep the meaning but change the form
```

Example:

```text
DIF: This may be a general page performance issue.
Human: Almost, but it happens specifically when switching markets.
```

The correction updates the current interpretation.

See: [`docs/safety.md`](safety.md)

---

## Correction

A `Correction` is a specific piece of human feedback on an interpretation.

Example:

```text
Not the whole page. The issue happens when users switch between markets.
```

A correction can accept, reject, narrow, modify, or reframe a hypothesis.

DIF must not ignore explicit correction.

See: [`docs/entities.md`](entities.md)

---

## Confirmed Intent

A `Confirmed Intent` is the current human-approved version of what should be acted on.

It is not eternal. It is versioned and can change later.

Example:

```text
Investigate delayed price updates and temporary UI freezing during market switching.
```

DIF should generate action only after the intent is confirmed enough.

See: [`docs/clarification-flow.md`](clarification-flow.md)

---

## Intent Graph

An `Intent Graph` is a structured map of the confirmed intent.

It can include goals, constraints, causes, conflicts, risks, options, and actions.

Example:

```text
Problem: Market switching feels slow
Symptom: Prices update with delay
Constraint: Do not expand into full dashboard redesign
Action: Create a testable engineering ticket
```

The graph helps keep the path from signal to action auditable.

See: [`docs/entities.md`](entities.md)

---

## Action Output

An `Action Output` is a concrete next step generated after clarification.

Examples:

- a testable GitHub issue;
- a product brief;
- a refined AI prompt;
- a support triage response;
- a roadmap item;
- a decision brief.

Example:

```text
Create a ticket with reproduction steps, expected behavior, actual behavior, missing context, and acceptance criteria.
```

See: [`docs/examples/vague-ticket.md`](examples/vague-ticket.md)

---

## Session

A `Session` is the full clarification journey.

It includes signals, context, hypotheses, corrections, confirmed intents, graphs, and actions.

Example path:

```text
raw signal -> context -> hypotheses -> correction -> confirmed intent -> graph -> action
```

A session preserves how the final action was reached.

See: [`schemas/session.schema.json`](../schemas/session.schema.json)

---

## Q-State Layer

The `Q-State Layer` is a quantum-inspired modeling layer for representing intention as an uncertain evolving state.

It does not require quantum computing.

It helps DIF model:

- uncertainty;
- competing meanings;
- context reduction;
- state transitions;
- meaning drift;
- action readiness.

Example:

```text
A vague request may contain several possible meanings at once: performance issue, UX issue, backend latency, or customer frustration.
```

See: [`docs/q-state-layer.md`](q-state-layer.md)

---

## Intent State Matrix

An `Intent State Matrix` is the current map of possible meanings behind one or more signals.

Example:

```text
Possible meanings:
- frontend performance issue: 0.35
- backend latency: 0.25
- websocket update delay: 0.25
- UX expectation gap: 0.15
```

It is not a final answer. It is a structured snapshot of uncertainty.

See: [`src/q-state/types.ts`](../src/q-state/types.ts)

---

## Partial Trace View

A `Partial Trace View` is one focused lens on the full intention state.

It reduces a complex signal into one useful perspective.

Example views:

```text
business view
technical view
emotional view
action view
QA/testability view
```

Example:

```text
Full signal: The page is slow and users are unhappy.
QA/testability view: Which flow is slow, how reproducible is it, and what are expected vs actual results?
```

See: [`docs/q-state-layer.md`](q-state-layer.md)

---

## Intent Channel

An `Intent Channel` is a transition from one intent state to another.

Clarification events can change the state:

- new signal;
- added context;
- clarification question;
- human correction;
- hypothesis accepted;
- hypothesis rejected;
- intent confirmed;
- action generated.

Example:

```text
raw vague complaint -> clarification question -> narrowed performance issue -> confirmed ticket intent
```

See: [`src/q-state/types.ts`](../src/q-state/types.ts)

---

## Decoherence Radar

`Decoherence Radar` detects meaning drift.

It asks:

```text
Are we still acting on the confirmed intent, or did we drift into a different task?
```

Example:

```text
Confirmed intent:
Investigate delayed updates during market switching.

Drifted output:
Redesign the entire dashboard.

Radar result:
High drift risk. Ask for confirmation before expanding scope.
```

See: [`docs/decoherence-radar.md`](decoherence-radar.md)

---

## Clarity Gain

`Clarity Gain` measures whether the clarification process made the signal more understandable and actionable.

Example:

```text
Before: vague complaint with no page, user, or reproduction path.
After: confirmed issue with affected flow, symptoms, missing context, and next action.
```

Clarity gain should not mean false certainty. It should mean the human-confirmed interpretation became clearer.

See: [`docs/q-state-layer.md`](q-state-layer.md)

---

## Actionability Score

`Actionability Score` estimates whether a confirmed intent is ready to become a task, prompt, plan, ticket, or decision.

Useful checks:

```text
Is the goal clear?
Is the domain clear?
Are constraints known?
Is there a next action?
Are risks visible?
Has the human confirmed the interpretation?
```

Example:

```text
Actionability Score: medium-high
Recommendation: create a GitHub-ready issue, but keep missing context explicit.
```

See: [`src/q-state/types.ts`](../src/q-state/types.ts)

---

## Drift

`Drift` is the loss of connection between the original signal, confirmed intent, and current output.

Example:

```text
Original signal: Checkout fails after clicking Pay.
Confirmed intent: Investigate payment button spinning indefinitely.
Drifted action: Send generic browser cache instructions.
```

DIF should detect drift and ask for confirmation before acting further.

See: [`docs/decoherence-radar.md`](decoherence-radar.md)

---

## False Certainty

`False Certainty` happens when a system presents an uncertain interpretation as if it were final truth.

Unsafe:

```text
You definitely want to rebuild the dashboard.
```

Safer:

```text
One possible interpretation is that the dashboard flow needs investigation. Is that correct, partly correct, or wrong?
```

Avoiding false certainty is central to DIF safety.

See: [`docs/safety.md`](safety.md)

---

## Summary

DIF is built around a simple path:

```text
Signal
-> Context
-> Meaning Hypotheses
-> Human Correction Loop
-> Confirmed Intent
-> Intent Graph
-> Action Output
```

The Q-State Layer extends this with a language for uncertainty, transitions, and drift:

```text
Intent State Matrix
-> Partial Trace Views
-> Intent Channels
-> Decoherence Radar
```

But the invariant stays the same:

```text
No system has final authority over human intention.
```
