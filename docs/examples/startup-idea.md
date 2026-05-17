# Example: Startup Idea to Product Direction

**Use case:** founders, builders, product teams  
**Goal:** Show how DIF turns a messy early idea into a clarified product direction.

---

## Raw Signal

```text
I have an AI idea but I do not know if it is a product, protocol, or research direction.
```

This signal contains energy and direction, but it is not yet a decision.

---

## Visible Signals

```json
{
  "visibleSignals": [
    "The user has an AI-related idea.",
    "The idea has multiple possible forms.",
    "The user is unsure whether to build a product, protocol, or research direction.",
    "The desired first audience is not yet clear.",
    "The next action is not yet defined."
  ]
}
```

---

## Meaning Hypotheses

```json
{
  "meaningHypotheses": [
    {
      "id": "hypothesis_product",
      "text": "The user may want to turn the idea into a practical product with a clear user and use case.",
      "confidence": "medium",
      "status": "proposed"
    },
    {
      "id": "hypothesis_protocol",
      "text": "The user may want to define a reusable protocol or architecture layer for others to build on.",
      "confidence": "medium",
      "status": "proposed"
    },
    {
      "id": "hypothesis_research",
      "text": "The user may want to frame the idea as a research direction or technical thesis.",
      "confidence": "medium",
      "status": "proposed"
    }
  ]
}
```

---

## Clarifying Questions

```text
1. Who should benefit first: founders, product teams, QA/support teams, or AI-agent developers?
2. Should the first version be a demo, a document, an API, or a CLI?
3. Is the main value clarity, safety, productivity, or research novelty?
4. What would make the idea understandable in 60 seconds?
5. What is the smallest useful output the system can produce?
```

---

## Human Correction

Example human response:

```text
It should become a product first, not just a research note. The first audience should be teams that use AI and lose time because requests are vague.
```

DIF updates the interpretation:

```json
{
  "correction": {
    "effect": "choose_direction",
    "rejectedInterpretations": [
      "research_only",
      "protocol_first"
    ],
    "strengthenedInterpretations": [
      "product_first",
      "teams_using_ai",
      "vague_request_clarification"
    ]
  }
}
```

---

## Confirmed Intent

```text
Create a product that helps teams clarify vague human requests before AI systems or teams act on them.
```

Human confirmation example:

```text
Yes. Start from a simple Task Clarifier demo.
```

---

## Action Output

### Product Wedge

```text
DIF Task Clarifier
```

### Promise

```text
Turn vague requests into confirmed intent, missing context, acceptance criteria, and one concrete next action.
```

### First User

```text
Small AI-first product, QA, support, or engineering teams.
```

### First Demo Flow

```text
1. User pastes a vague request.
2. DIF extracts visible signals.
3. DIF proposes meaning hypotheses.
4. User corrects or confirms.
5. DIF generates a task-ready output.
6. DIF checks for meaning drift before action.
```

### Next Action

```text
Create three example sessions showing before/after transformations.
```

---

## Decoherence Check

Potential drift:

```text
Original confirmed intent:
Create a product for clarifying vague requests before execution.

Drifted direction:
Build a broad personal reflection app for every possible inner state.
```

Radar result:

```json
{
  "risk": "medium",
  "reason": "The direction expanded from a concrete team workflow into a broad personal product.",
  "recommendedQuestion": "Should the first version stay focused on team task clarification?"
}
```

---

## Why This Example Matters

```text
messy startup idea -> clarified product wedge -> first demo flow -> next action
```

DIF helps the founder avoid building the wrong first version.
