---
id: platform-codex-local-memory-default
title: Codex Local Memory Source Default
summary: Use local layered memories as the default source in this runtime.
layer: platform
scope: runtime
applies_to: codex
type: procedure
stability: high
source:
  - sanitized-example
evidence:
  - consistent routing behavior across sessions
regression_risk: low
supersedes: []
last_reviewed: 2026-04-19
owner: team
status: active
sync:
  codex: yes
  other_runtime: no
---

## What

Use local memory root first for identity/preferences/continuity queries.

## Why

Avoids external memory routing drift.

## When To Apply

All memory-related lookups in Codex runtime.

## When Not To Apply

Tasks explicitly scoped to external memory systems.

## Review / Downgrade Conditions

Review if runtime memory behavior changes.
