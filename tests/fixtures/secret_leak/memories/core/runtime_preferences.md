---
id: core-runtime-preferences
title: Runtime Preferences
summary: Secret leak fixture.
layer: core
scope: global
applies_to: all
type: preference
stability: high
source:
  - fixture
evidence:
  - ghp_abcdefghijklmnopqrstuvwxyz1234567890
regression_risk: medium
supersedes: []
last_reviewed: 2026-04-28
owner: team
status: active
---

# Runtime Preferences

- This fixture intentionally leaks a fake token-shaped string.
