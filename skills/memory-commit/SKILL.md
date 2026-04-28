---
name: memory-commit
description: Use after a distillation pass already produced a canonical candidate list and the main question is where accepted items should land after reject-only user feedback.
---

# Memory Commit

## Overview

Run this skill after distillation, not before.
It is a thin execution layer: normalize reject-only feedback, route accepted items, write the minimum necessary updates, and emit a Commit Report.

## Workflow

1. Read the distillation result and canonical candidate list.
2. Normalize reject-only user feedback into candidate IDs.
3. Treat non-rejected candidates as accepted.
4. Route accepted candidates to rollout retrospectives, work memory, or personal memory.
5. Ask one clarification question only when work-memory vs personal-memory routing is high-risk and genuinely ambiguous.
6. Write the minimum necessary updates.
7. Produce a Commit Report.

## Boundary

- Do not re-distill raw chat from scratch.
- Do not re-score or re-rank candidates.
- Do not replace the existing truth-source files with policy copied into this skill.

## Required References

- Read [contract.md](./contract.md)
- Read [references/routing-and-clarification.md](./references/routing-and-clarification.md)
- Read [examples/minimal-commit-report.md](./examples/minimal-commit-report.md)
