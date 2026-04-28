---
id: learning-memory-pollution
title: Memory Pollution from Local Noise
summary: Local task noise should not be promoted into durable core memory.
layer: learnings
scope: learning
applies_to: all
type: learning
stability: medium
source:
  - sanitized-example
evidence:
  - repeated false generalization incidents
regression_risk: medium
supersedes: []
last_reviewed: 2026-04-19
owner: team
status: active
sync:
  codex: yes
  other_runtime: optional
---

## What

Prevent one-off local details from entering durable layers.

## Why

Reduces long-term drift and maintenance burden.

## When To Apply

Every memory write decision.

## When Not To Apply

When local detail is intentionally repo-scoped and versioned.

## Review / Downgrade Conditions

Downgrade if rule becomes redundant with automated checks.
