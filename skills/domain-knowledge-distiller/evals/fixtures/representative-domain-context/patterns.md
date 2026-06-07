---
id: representative-domain-patterns
title: Representative Patterns
summary: Synthetic patterns for richer fixture validation.
scope: runtime
applies_to: codex
type: pattern
stability: medium
status: active
last_reviewed: 2026-06-07
retrieval_keys:
  - representative pattern
  - conflict routing
---

# Patterns

## Source-Tension Routing

- claim: When sources conflict, preserve the disagreement as a routing object instead of forcing consensus.
- mechanism: Future agents need to know when a domain has stable rules and when it has unresolved tradeoffs.
- use_when:
  - Two credible sources disagree about a mechanism or boundary.
- do_not_use_when:
  - The conflict is only wording-level and does not change future action.
- retrieval_keys:
  - conflicting sources
  - unresolved tradeoff
  - source tension
- source_refs:
  - synthetic-field-report
  - synthetic-review-paper
- confidence: high
- last_reviewed: 2026-06-07
