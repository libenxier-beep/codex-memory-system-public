# Router Prompt Template

Use this template when turning a parsed intake item into a KHub decision.

## Goal

Return either:

- one `route-plan`, or
- one `decision-report`

## Rules

- never force an item into a mismatched template
- never write Obsidian content directly
- use `no_fit` when KHub has no reliable slot
- use `needs_human_decision` when multiple plausible paths remain too close
- set `write_blocked: true` for all blocked states
- apply `../workflow-principles.md` for template-density decisions

## Inputs

- parsed intake item
- available KHub note types
- available KHub areas and buckets
- available templates
- duplicate or append candidates

## Output Shape

Follow `templates/route-plan.schema.yaml` or `templates/decision-report.schema.yaml`.
