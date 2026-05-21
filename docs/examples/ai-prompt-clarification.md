# Example: AI Prompt Clarification

**Use case:** AI users, founders, product teams, marketers, and builders  
**Goal:** Show how DIF clarifies a vague AI prompt before generation.

---

## Raw Signal

```text
Write me a landing page for my startup.
```

This looks like a normal AI prompt, but it is still under-specified.

A regular AI tool may immediately generate a generic landing page.

DIF should start earlier:

```text
raw signal -> visible signals -> missing context -> meaning hypotheses -> human correction -> confirmed intent -> better prompt
```

---

## Visible Signals

DIF first extracts what is visible without pretending to know the full intent.

```json
{
  "visibleSignals": [
    "The user wants a landing page.",
    "The page is for a startup.",
    "The startup category is not specified.",
    "The target audience is not specified.",
    "The conversion goal is not specified.",
    "The desired tone is not specified.",
    "The stage of the startup is unknown.",
    "The user may need a product brief before copywriting."
  ]
}
```

---

## Missing Context

Before generating copy, DIF should identify missing context.

```text
- What does the startup do?
- Who is the landing page for?
- What should visitors do after reading it?
- Is the goal waitlist signup, demo booking, investor interest, hiring, or developer adoption?
- What makes the product different?
- What tone should the page use?
- Is there an existing product, prototype, or only an idea?
```

---

## Initial Meaning Hypotheses

DIF proposes possible interpretations instead of choosing one too early.

```json
{
  "meaningHypotheses": [
    {
      "id": "hypothesis_marketing_page",
      "text": "The user may want marketing copy for a public landing page.",
      "confidence": "medium",
      "status": "proposed"
    },
    {
      "id": "hypothesis_product_positioning",
      "text": "The user may actually need product positioning before the landing page can be written well.",
      "confidence": "medium",
      "status": "proposed"
    },
    {
      "id": "hypothesis_investor_page",
      "text": "The user may want a page that explains the startup to investors or partners.",
      "confidence": "low",
      "status": "proposed"
    },
    {
      "id": "hypothesis_waitlist_page",
      "text": "The user may want a waitlist page for early users.",
      "confidence": "low",
      "status": "proposed"
    }
  ]
}
```

---

## Clarifying Questions

DIF should ask a small number of high-leverage questions.

```text
1. What does the startup do in one sentence?
2. Who is the first target audience?
3. What is the primary CTA: join waitlist, book demo, try product, read docs, or contact you?
4. What should the page emphasize: pain, product, trust, demo, technical depth, or business value?
5. What tone should it use: concise, bold, technical, investor-friendly, friendly, premium, or experimental?
```

---

## Human Correction

Example human response:

```text
It is not a generic startup. It is an AI tool that clarifies vague human requests before AI or teams act. The first audience is product, QA, support, and engineering teams. The CTA should be to try a Task Clarifier demo or read examples.
```

DIF treats this as correction and context, not as a separate request.

```json
{
  "correction": {
    "effect": "narrow_scope",
    "rejectedInterpretations": [
      "generic_startup_page",
      "investor_only_page"
    ],
    "strengthenedInterpretations": [
      "ai_intent_clarification_tool",
      "task_clarifier_demo",
      "product_qa_support_engineering_audience"
    ]
  }
}
```

---

## Confirmed Intent

After correction, DIF can propose a confirmed intent.

```text
Create a landing page brief for an AI intent clarification tool that helps product, QA, support, and engineering teams turn vague requests into confirmed intent and action-ready tasks before AI or teams execute.
```

Human confirmation example:

```text
Yes. Make the prompt specific enough for an AI copywriter to generate a useful landing page.
```

---

## Intent Graph

```json
{
  "nodes": [
    {
      "id": "goal_landing_page",
      "type": "goal",
      "label": "Generate a useful landing page brief"
    },
    {
      "id": "audience_teams",
      "type": "value",
      "label": "Product, QA, support, and engineering teams"
    },
    {
      "id": "problem_vague_requests",
      "type": "cause",
      "label": "Vague requests lead to wrong AI or team execution"
    },
    {
      "id": "constraint_not_generic",
      "type": "constraint",
      "label": "Do not write a generic startup page"
    },
    {
      "id": "action_improved_prompt",
      "type": "action",
      "label": "Generate an improved AI prompt for landing page copy"
    }
  ],
  "edges": [
    {
      "from": "problem_vague_requests",
      "to": "goal_landing_page",
      "type": "supports"
    },
    {
      "from": "constraint_not_generic",
      "to": "action_improved_prompt",
      "type": "protects"
    },
    {
      "from": "audience_teams",
      "to": "action_improved_prompt",
      "type": "clarifies"
    }
  ]
}
```

---

## Action Output: Improved AI Prompt

Instead of sending the raw prompt:

```text
Write me a landing page for my startup.
```

DIF produces a more actionable prompt:

```text
Write a landing page for DeepIntent Funnel (DIF), an AI intent clarification layer for product, QA, support, and engineering teams.

The page should explain that many AI and engineering failures start before execution: vague human input, unclear tasks, missing context, and hidden assumptions.

Position DIF as a system that transforms raw human signals into clarified intent, structured meaning, and action-ready output before AI tools or teams act.

Primary audience:
- product managers;
- QA engineers;
- support leads;
- engineering managers;
- AI-first startup teams.

Core message:
Clarify human intent before AI or teams act.

Use the flow:
raw signal -> visible signals -> meaning hypotheses -> human correction -> confirmed intent -> action output.

Include a concrete example:
Input: "The page is slow and users are unhappy."
DIF output: missing context, clarifying question, confirmed intent, testable engineering ticket, and drift check.

Primary CTA:
Try the Task Clarifier demo or read the examples.

Tone:
Clear, precise, practical, developer-friendly, not hype-driven.

Avoid:
- claiming mind reading;
- saying the system knows the user's true intent;
- presenting DIF as therapy;
- overusing quantum language;
- generic startup buzzwords.

Required sections:
1. Hero
2. Problem
3. Solution
4. How it works
5. Example
6. Use cases
7. Safety principle
8. CTA
```

---

## Decoherence Check

DIF should detect if the improved prompt drifts from the confirmed intent.

Potential drift:

```text
Confirmed intent:
Create a landing page brief for an AI intent clarification tool for product, QA, support, and engineering teams.

Drifted output:
Create a spiritual AI assistant that understands the soul of every user.
```

Radar result:

```json
{
  "risk": "high",
  "reason": "The output moved from practical team intent clarification into a broad spiritual assistant framing that was not confirmed.",
  "recommendedQuestion": "Should the page stay focused on practical team workflows and vague request clarification?"
}
```

---

## Why This Example Matters

This example shows the core DIF value for everyday AI use:

```text
vague prompt -> clarified intent -> better prompt -> safer generation
```

DIF does not replace the generator.

DIF improves the input before generation.

The goal is not to answer faster.

The goal is to act on the right intent.
