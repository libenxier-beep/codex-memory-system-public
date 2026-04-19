# 03 记忆生命周期

## 生命周期闭环

1. 观察交互结果
2. 提取候选洞察
3. 判定 scope 与稳定性
4. 与现有记忆比较
5. 决策 `add | merge | upgrade | split | discard`
6. 路由到目标层
7. 记录结构性变更
8. 周期性复核

## 去重决策

- `revalidate`：同一规则，无实质增量
- `merge`：同一范围，但边界/表达更清晰
- `upgrade`：新规则明显优于旧规则
- `split`：表面相似但适用范围不同
- `discard`：低信号、本地化、易失真或风险高

## 退役决策

- 当规则不再中性时，`core -> platform`
- 当规则变成临时状态时，`core/platform -> short_term`
- 被替代时标记 `superseded`，不直接删除
