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

### Ring 3 (cold memory)
Load only for explicit retrieval or incident reconstruction.

## Recall-first behavior

When user asks about previous work (e.g., "last time", "before"), do retrieval first:

1. check curated memory index/summaries
2. retrieve relevant rollout/session evidence
3. answer with evidence-aware summary

## Routing priority

1. Scope correctness
2. Conflict avoidance
3. Single source-of-truth preservation
4. Low maintenance cost
