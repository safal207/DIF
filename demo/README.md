# DIF Task Clarifier Demo

This is a dependency-free browser demonstration of the DeepIntent Funnel flow.

It shows this sequence:

```text
raw signal
-> visible signals
-> missing context
-> clarification questions
-> meaning hypotheses
-> human correction
-> confirmed intent
-> action-ready ticket
-> drift check
```

## Run locally

No installation is required.

1. Download or clone the repository.
2. Open `demo/index.html` in a modern browser.
3. Enter a vague task, complaint, or product request.
4. Review the proposed clarification.
5. Select a meaning hypothesis and add a correction when needed.
6. Confirm the intent and inspect the ticket draft.

## Prototype boundary

The page uses deterministic browser-side rules and does not call an external model.

Its purpose is to make the DIF interaction pattern visible and testable before heavier infrastructure is introduced.

## Main invariant

```text
No system has final authority over human intention.
```

The human can confirm, correct, or reject the proposed interpretation.
