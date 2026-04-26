# 01 架构

## 核心思想

采用分层记忆架构，而不是堆积完整对话转录。

- 长期记忆应显式、结构化。
- 会话上下文应临时、隔离。
- 平台差异应通过适配层处理，避免污染中性规则。

## 主要组件

1. 记忆分层
- `core`：中性、长期、可复用规则
- `platform`：环境/运行时特定适配规则
- `learnings`：可复用经验与高频失败模式
- `rollout_summaries`：完整回合复盘与待晋升结论

2. 运行时 sidecar
- `memory-sidecar/evidence`：原始或近原始执行证据
- `memory-sidecar/sessions`：session 级压缩运行态
- `memory-sidecar/indexes`：当前/最近查询入口
- `memory-sidecar/policies`：读取、晋升、保留规则

3. 协议文件
- `memory_index.md`：主索引与真源声明
- `memory_schema.md`：记忆条目结构规范
- `memory_intake_checklist.md`：写入门禁
- `memory_change_log.md`：结构变更审计日志

4. 执行技能
- `forge`：把材料转成长期升级
- `post-collaboration-distillation`：任务后保守沉淀
- `mem-search`：跨会话召回流程

## 为什么这样设计

- 在长任务中保持记忆可用
- 减少重复回放整段上下文的 token 浪费
- 通过范围与生命周期分离降低规则漂移
- 避免 handoff、运行时证据、回合复盘、长期记忆被塞进同一个模糊容器
