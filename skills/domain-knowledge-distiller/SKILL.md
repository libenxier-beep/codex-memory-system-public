---
name: domain-knowledge-distiller
description: Use when a user asks to absorb, distill, internalize, deconstruct, or abstract reusable principles, patterns, philosophy, architecture, or tactics from articles, architectures, quotes, failure cases, or other high-value resources into durable work_contexts knowledge for future agent use; includes triggers like 吸收, 沉淀, 内化, 解构, 抽象成原则, 以后能用, 放进work_contexts.
---

# Domain Knowledge Distiller

## Use When

- The user wants high-value resources transformed into reusable domain knowledge, not just summarized.
- The target output is a durable `work_contexts/<domain_slug>/` mini wiki.
- The work needs first-principles analysis, reusable principles, patterns, case mechanisms, architecture, micro tactics, or future retrieval metadata.
- The user explicitly asks for future agent use, efficient recall, knowledge routing, or a Karpathy-style LLM wiki.

## Do Not Use When

- The user only asks for a normal summary, translation, rewrite, excerpt, or temporary reading note.
- The source is low-value and the user has not asked to preserve it.
- The task is only factual verification, citation collection, or web research without durable distillation.
- The knowledge belongs in a repo-local `AGENTS.md`, a one-off prompt, or a deterministic script instead of a reusable domain context.

## Procedure

1. Identify the target domain and source set.
   - If the domain is unclear and cannot be inferred from the task, ask one concise question.
   - Treat explicit requests like "save", "put into work_contexts", or "make this reusable later" as authorization to update that domain context.
2. Assess source quality and fit.
   - For external or current sources, verify with web access when needed and keep source links.
   - Read `references/source-quality-rubric.md` when source credibility, conflict, or copyright handling matters.
3. Distill by mechanism, not by surface summary.
   - Read `references/first-principles-distillation.md` for deep decomposition.
   - Extract goals, constraints, causal mechanisms, invariants, tradeoffs, failure boundaries, and transfer limits.
4. Encode for future agent use.
   - Read `references/agent-learning-loop.md` when building durable knowledge cards.
   - Each important item needs future-use metadata: use cases, non-use cases, retrieval keys, source refs, confidence, and last reviewed date.
5. Route into a domain mini wiki.
   - Default path: `/Users/liben/.codex/memories/work_contexts/<domain_slug>/`.
   - Read `references/retrieval-routing.md` before creating or restructuring the wiki.
   - Use templates from `templates/` when creating new pages or cards.
6. Validate the result.
   - Run `python3 scripts/lint_domain_context.py <domain_context_path>` when files are created or edited.
   - Perform one retrieval pressure check: given a future task prompt, verify that `README.md -> index.md/retrieval.md -> target page` finds the relevant knowledge.

## Read Only If Needed

- `references/first-principles-distillation.md`: Use for deep decomposition and abstraction quality.
- `references/agent-learning-loop.md`: Use when converting sources into future-callable knowledge cards.
- `references/retrieval-routing.md`: Use when creating or maintaining `work_contexts/<domain_slug>/`.
- `references/source-quality-rubric.md`: Use when judging source quality, provenance, conflicts, or copyright boundaries.
- `templates/`: Use when creating a new domain context or adding structured knowledge cards.
- `schemas/`: Use when checking structured fields, source manifest entries, or frontmatter.
- `evals/prompts.csv`: Use when testing trigger behavior and retrieval quality.
- `scripts/lint_domain_context.py`: Run after writing or modifying a domain context.

## Output Contract

Return:

- Target domain and source set.
- What was absorbed, what was rejected or deferred, and why.
- New or updated reusable knowledge: principles, patterns, architecture, micro tactics, cases, open questions.
- Future-use routing: likely user triggers, retrieval keys, first page to read, and pages updated.
- Evidence: changed files, lint result, and one retrieval pressure check.

## Validation

- Explicit trigger: "Use domain-knowledge-distiller to absorb this article into work_contexts."
- Implicit trigger: "This failure case is valuable; turn it into principles I can use later."
- Negative control: "Summarize this article in 300 words."
- Evidence check: The output includes source provenance, knowledge cards, retrieval keys, updated index/retrieval pages, and a successful lint run.

## Common Mistakes

- Producing a polished summary but no reusable mechanism, boundary, or retrieval metadata.
- Copying whole articles into memory instead of storing compact source cards, links, short excerpts, and derived knowledge.
- Putting every domain into one large wiki instead of one `work_contexts/<domain_slug>/` per domain.
- Making `README.md` a tutorial; keep it an entry point with shortest read paths.
- Writing principles without non-use cases, source refs, or confidence.
