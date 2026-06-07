# First-Principles Distillation

Use this when source material is valuable enough to become future operating knowledge.

## Distillation Target

Do not ask "what does the source say?" first. Ask:

- What problem is it solving?
- What constraints make this problem hard?
- What mechanism makes the proposed answer work?
- What changes if the context changes?
- What would fail if we copied the surface form?

## Decomposition Pass

Extract these fields before writing durable knowledge:

| Field | Question |
| --- | --- |
| Goal | What outcome is the source trying to improve? |
| User or system | Who or what receives value? |
| Constraints | What scarcity, risk, friction, or dependency shapes the solution? |
| Mechanism | What causal chain makes the idea work? |
| Invariants | What remains true across contexts? |
| Variables | What must be adapted per domain, audience, model, or tool? |
| Tradeoffs | What gets better, and what gets worse? |
| Failure modes | Where does this idea break or mislead? |
| Transfer test | What other domain would this help, and what would need to change? |

## Knowledge Types

Route extracted knowledge by type:

- Principle: stable judgment rule or philosophy.
- Pattern: repeatable method, shape, sequence, or decomposition.
- Architecture: macro structure, routing, state, ownership, data flow, or layering.
- Micro tactic: phrase, checklist, local heuristic, prompt move, UI detail, or review move.
- Case: specific success or failure analyzed for mechanism.
- Open question: important uncertainty that should not be promoted yet.

## Abstraction Quality Bar

A useful abstraction is:

- More general than the source but not generic.
- Specific enough to change future behavior.
- Paired with use cases and non-use cases.
- Connected to source evidence and confidence.
- Written so a future agent can apply it without rereading the original source.

## Output Shape

Prefer compact knowledge cards:

```markdown
### <short claim>

- claim:
- mechanism:
- use_when:
- do_not_use_when:
- retrieval_keys:
- source_refs:
- confidence:
- last_reviewed:
```

Use prose only after the card if the mechanism needs explanation.
