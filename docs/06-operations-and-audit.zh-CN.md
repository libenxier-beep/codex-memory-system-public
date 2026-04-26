# 06 运维与审计

## 运维例行项

- 仅在有意义会话后运行任务后沉淀
- 信号弱时优先输出 summary-only
- 会话历史与长期记忆保持隔离
- 默认把长任务的滚动 handoff 放在项目内 `docs/progress.md`
- 只有当下一步队列太吵、影响扫描速度时，才拆出单独的 `docs/next_steps.md`
- 运行时证据放 `memory-sidecar/`，完整回合复盘放 `rollout_summaries/`

## 审计工件

- 结构性更新写入 change log
- rollout/session summaries 作为证据链
- schema/checklist 作为策略契约文件

## 推荐指标

1. 分类正确率（是否进正确层）
2. 去重质量（近重复是否下降）
3. 污染率（无效长期写入比例）
4. 检索有效性（召回证据是否可用）
