# 03 记忆生命周期

## 生命周期闭环

1. 采集运行时证据
2. 压缩一个有边界的 session
3. 写出完整 rollout 复盘
4. 提取候选洞察
5. 判定 scope 与稳定性
6. 与现有记忆比较
7. 决策 `add | merge | upgrade | split | discard`
8. 路由到目标层
9. 记录结构性变更
10. 周期性复核

## 分层晋升路径

- `memory-sidecar/evidence` -> 原始或近原始痕迹
- `memory-sidecar/sessions` -> 压缩后的运行时上下文
- `memories/rollout_summaries` -> 完整复盘与待晋升结论
- 长期记忆层 -> 最终稳定产物

## 去重决策

- `revalidate`：同一规则，无实质增量
- `merge`：同一范围，但边界/表达更清晰
- `upgrade`：新规则明显优于旧规则
- `split`：表面相似但适用范围不同
- `discard`：低信号、本地化、易失真或风险高

## 退役决策

- 当规则不再中性时，`core -> platform`
- 当结论被证明只是临时或局部状态时，回退到 runtime sidecar
- 被替代时标记 `superseded`，不直接删除
