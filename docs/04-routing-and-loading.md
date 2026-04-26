# 04 Routing and Loading

## Progressive loading (Ring model)

### Ring 0 (always load)
- memory index
- global principles
- runtime preferences
- current platform adapter

### Ring 1 (task-routed)
Load 1-2 files depending on task type (skill engineering, memory architecture, evaluation, orchestration, etc.).

### Ring 2 (deep reference)
Load only when needed for concrete decisions.
- Query `memory-sidecar/` only when the task is about current activity, recent session state, or evidence backtracking.

### Ring 3 (cold memory)
Load only for explicit retrieval or incident reconstruction.

## Recall-first behavior

When user asks about previous work (e.g., "last time", "before"), do retrieval first:

1. check curated memory index/summaries
2. retrieve relevant rollout/session evidence
3. answer with evidence-aware summary

## Runtime lookup order

1. project `docs/progress.md` for current handoff
2. `memory-sidecar/indexes/` for current/recent lookup
3. `memory-sidecar/sessions/` for compressed runtime context
4. `memory-sidecar/evidence/` only when raw proof is required

## Personal-memory routing

- Default to `personal_memory/` for life, state, growth, relationship, or self-understanding requests.
- Read both work memory and personal memory only when the user question explicitly crosses work decisions and personal state.
- Keep private signals out of work-facing durable memory unless the user explicitly wants a cross-domain synthesis.

## Routing priority

1. Scope correctness
2. Conflict avoidance
3. Single source-of-truth preservation
4. Low maintenance cost
