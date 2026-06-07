---
id: "{{domain_slug}}-agent-rules"
title: "{{domain_title}} Agent Rules"
summary: "Runtime behavior rules for agents using {{domain_title}}."
scope: runtime
applies_to: codex
type: agent-rules
stability: medium
status: active
last_reviewed: "{{YYYY-MM-DD}}"
retrieval_keys:
  - "{{domain_slug}} agent rules"
---

# Agent Rules

- Load this context only when the current task matches the domain scope.
- Start with `README.md`, then use `index.md` or `retrieval.md` to find the smallest needed page.
- Do not load the whole folder unless the user asks for an audit or restructure.
- When applying knowledge, distinguish verified principles, source-derived inference, and current-task assumptions.
- Preserve source refs and confidence when using a claim.
- Add new durable knowledge only when it changes future behavior.
- Put uncertain or weakly sourced claims in `open_questions.md`.
