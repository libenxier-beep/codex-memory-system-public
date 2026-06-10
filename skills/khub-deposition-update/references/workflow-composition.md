# Workflow Composition

## Upstream Contract

This skill only consumes a validated `route-plan` from `khub-classifier-router`.

## Refusal Cases

Refuse execution when upstream returns:

- `no_fit`
- `needs_human_decision`
- `write_blocked: true`

## Downstream Contract

When execution is allowed:

1. render note content through `obsidian-markdown`
2. execute note operations through `obsidian-cli`
3. return an `execution-report`

When execution is refused:

1. do not call write operations
2. return a blocked or conflict outcome

## Principle Reference

- Cross-layer workflow principles live in `../workflow-principles.md`.
- This file describes composition order only; it is not the source of truth for fidelity or template-density rules.
