# Retrieval Routing

Use this when building or updating a domain context under:

`/Users/liben/.codex/memories/work_contexts/<domain_slug>/`

## Default Mini Wiki

```text
work_contexts/<domain_slug>/
  README.md
  index.md
  AGENT.md
  principles.md
  patterns.md
  architecture.md
  micro_tactics.md
  casebook.md
  retrieval.md
  open_questions.md
  log.md
  sources/
    manifest.jsonl
```

## Page Roles

| Page | Role |
| --- | --- |
| `README.md` | Entry point, domain scope, shortest read paths. |
| `index.md` | Lookup by task, concept, scene, failure mode, and source. |
| `AGENT.md` | Behavior rules for agents working inside this domain. |
| `principles.md` | Stable domain philosophy and judgment rules. |
| `patterns.md` | Reusable methods, moves, and operating patterns. |
| `architecture.md` | Macro structure, routing, state, layering, data flow. |
| `micro_tactics.md` | Phrases, local heuristics, detail-level craft. |
| `casebook.md` | Success and failure cases with mechanisms. |
| `retrieval.md` | Trigger phrases, keywords, reverse index, route table. |
| `open_questions.md` | Unresolved claims, weak evidence, future validation. |
| `log.md` | Append-only update notes. |
| `sources/manifest.jsonl` | Source metadata, provenance, confidence, and refs. |

## Routing Rules

- Keep `README.md` small. It should tell the agent whether this domain applies and what to read next.
- Put search terms in frontmatter, headings, knowledge cards, and `retrieval.md`.
- Every durable claim needs a source ref or a clear "inference" marker.
- If a page grows because it covers unrelated tasks, split by knowledge type or task route.
- If the future agent would need the same two pages every time, summarize the shared rule in `README.md` and link to both.

## Retrieval Keys

Each knowledge card should include:

- Task language: phrases the user might type.
- Concept language: domain terms and synonyms.
- Failure language: symptoms, anti-patterns, mistakes.
- Artifact language: file names, page names, schemas, tools, or outputs.

Example:

```yaml
retrieval_keys:
  - absorb article into work_contexts
  - first-principles distillation
  - future agent recall
  - source-to-wiki
```

## Retrieval Pressure Check

After writing, test one future prompt:

1. State the prompt.
2. Identify which domain `README.md` should be read.
3. Identify which row in `index.md` or `retrieval.md` should route the agent.
4. Identify the exact target page and card.
5. If any step is unclear, patch routing now.

## Source Handling

- For web sources, store URL, title, author or organization, accessed date, short summary, and derived insights.
- Do not paste full copyrighted articles.
- Use short quotations only when necessary and within applicable limits.
- For user-provided private material, record provenance without exposing sensitive content beyond the user's intended storage boundary.
