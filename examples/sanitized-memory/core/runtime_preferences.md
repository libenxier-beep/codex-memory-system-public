---
id: runtime-pref-recall-first
title: Recall First for Prior-Work Questions
summary: Retrieve prior evidence before asking follow-up questions for historical queries.
scope: core
applies_to: all
type: preference
stability: high
source:
  - sanitized-example
evidence:
  - repeated quality improvement in historical Q&A
regression_risk: low
supersedes: []
last_reviewed: 2026-04-19
owner: team
status: active
sync:
  codex: yes
  other_runtime: optional
---

## What

For "last time / before" style questions, perform retrieval first.

## Why

Improves factual grounding and reduces hallucinated history.

## When To Apply

Historical or continuity-sensitive queries.

## When Not To Apply

Purely present-tense or creative requests with no historical dependency.

## Review / Downgrade Conditions

Downgrade if retrieval tooling is unavailable or repeatedly unreliable.
