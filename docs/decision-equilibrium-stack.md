# Human-AI Decision Equilibrium Stack

**Status:** conceptual bridge  
**Scope:** relation between DIF, future DI, and DRP

This document explains how DeepIntent Funnel (DIF) relates to two neighboring layers:

- **DI** — Decision / Domain Intelligence for capabilities and limitations;
- **DRP** — Decision Record Protocol for committed decisions and decision memory.

The goal is to make the project map explicit before creating more repositories or adding more implementation layers.

---

## Core Idea

Human-AI systems often fail because they move from vague input to action too quickly.

A safer path is:

```text
clarify intent -> clarify limits -> record decision -> act
```

In repository terms:

```text
DIF -> DI -> DRP
```

In system terms:

```text
intention -> feasible strategy space -> committed decision memory
```

---

## The Three Layers

## 1. DIF — Intent Clarification Layer

DIF answers:

```text
What does the human mean right now?
```

DIF works before action.

It transforms:

```text
raw signal -> meaning hypotheses -> human correction -> confirmed intent
```

DIF prevents premature execution based on vague prompts, unclear tickets, emotional complaints, or incomplete product requests.

Example:

```text
Raw signal:
The page is slow and users are unhappy.

DIF output:
Investigate delayed updates and UI freezing during the specific affected flow, before expanding scope into a full redesign.
```

DIF principle:

```text
Do not act before intention is clarified.
```

---

## 2. DI — Capability and Limitation Layer

DI is the future layer.

DI should answer:

```text
What is possible, impossible, risky, or bounded under current constraints?
```

DI should not replace DIF or DRP.

DI sits between clarified intent and committed decision.

It maps:

- available capabilities;
- missing capabilities;
- hard constraints;
- soft constraints;
- risks;
- feasibility;
- required approvals;
- irreversible steps;
- fallback options.

Example:

```text
Confirmed intent:
Build an AI support agent.

DI check:
The system can draft replies.
The system cannot send replies without human approval.
The system cannot access private customer data without permission.
The system must escalate billing and legal questions.
```

DI principle:

```text
Do not promise action before limitations are understood.
```

---

## 3. DRP — Decision Record Layer

DRP answers:

```text
What was decided, why, and how does it relate to previous decisions?
```

DRP works after intent and feasibility are clarified.

It records:

- what was decided;
- why it was decided;
- what alternatives were considered;
- what constraints mattered;
- what decision it supersedes;
- what future decision depends on it.

Example:

```text
Decision:
Start with support-agent draft replies only.

Reason:
Autonomous sending is too risky before trust, privacy, and escalation constraints are validated.

Supersession:
This replaces the earlier idea of fully autonomous support replies.
```

DRP principle:

```text
Do not let decisions disappear into memory or chat history.
```

---

## Nash-Inspired View

A Nash-style analysis asks:

```text
Who are the players?
What are their strategies?
What information do they have?
What incentives create drift?
What makes the result stable?
```

In human-AI work, the players are:

- the human;
- the AI system;
- the team or organization;
- the environment and constraints;
- future auditors or reviewers.

The unstable game looks like this:

```text
vague request -> confident AI output -> fast team action -> later disagreement
```

Common failure:

```text
The human did not mean that.
The AI assumed too much.
The team acted too early.
The limits were unclear.
The decision was not recorded.
```

The stable version requires three checks:

```text
1. Is the intent confirmed?
2. Are the constraints understood?
3. Is the decision recorded?
```

This creates an action equilibrium:

```text
confirmed intent + known constraints + recorded decision = stable action
```

---

## Stack Formula

```text
DIF + DI + DRP -> accountable human-AI action
```

Expanded:

```text
DIF clarifies what is meant.
DI clarifies what can and cannot be done.
DRP records what was decided and why.
```

Short form:

```text
Intent -> Limits -> Decision
```

---

## Example: AI Support Agent

### Raw signal

```text
Build me an AI agent for customer support.
```

### DIF step

DIF asks:

```text
Do you want automation, triage, draft replies, routing, analytics, or escalation?
```

Confirmed intent:

```text
Create an assistant that drafts support replies and suggests routing, but does not act autonomously yet.
```

### DI step

DI checks:

```text
Capabilities:
- Can draft replies.
- Can classify issue type.
- Can suggest routing.

Limitations:
- Cannot send without approval.
- Cannot access billing data without permission.
- Cannot answer legal questions.
- Must escalate angry enterprise customers.

Feasibility:
- MVP is feasible if limited to draft replies and routing suggestions.
```

### DRP step

DRP records:

```text
Decision:
Build support draft assistant first.

Why:
Lower risk, easier review, preserves human approval.

Rejected alternative:
Fully autonomous support agent.

Reason rejected:
Too much trust, privacy, and escalation risk.
```

---

## Boundaries Between Repositories

| Layer | Repository | Main question | Output |
|---|---|---|---|
| Intent | DIF | What is meant? | Confirmed intent |
| Limits | DI | What is possible or bounded? | Feasibility / capability map |
| Memory | DRP | What was decided and why? | Decision record |

---

## What DI Should Become

DI should be a narrow and clean repository.

Suggested thesis:

```text
DI maps what can and cannot be done before decisions become commitments.
```

Suggested structure:

```text
DI/
  README.md
  docs/
    concept.md
    capability-boundaries.md
    limitation-model.md
    relation-to-dif-and-drp.md
  schemas/
    capability.schema.json
    limitation.schema.json
    feasibility-check.schema.json
  examples/
    ai-agent-support.md
    startup-plan.md
    qa-automation.md
```

DI should not become a broad productivity system.

DI should stay focused on:

```text
capabilities, limits, feasibility, risk, and commitment boundaries
```

---

## Non-Goals

This stack should not claim:

- that the system knows the user's true intent;
- that all constraints can be known;
- that recorded decisions are automatically correct;
- that AI should act without human confirmation;
- that equilibrium means no future change.

A stable decision can still be revised.

Revision should happen through explicit correction, feasibility update, or decision supersession.

---

## Maintainer Rule

Before adding a new layer, ask:

```text
Which question does this layer answer?
```

If the answer is intent, it belongs near DIF.

If the answer is capability or limitation, it belongs near DI.

If the answer is decision memory, it belongs near DRP.

If it answers none of these, it may be a separate project or should wait.

---

## Summary

DIF, DI, and DRP can form a simple decision stack:

```text
DIF — do not act before intent is clarified.
DI  — do not promise action before limits are understood.
DRP — do not forget why the decision was made.
```

Together:

```text
clarify intent -> clarify limits -> record decision -> act with accountability
```
