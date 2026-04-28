# 10 案例链路

## 目标

用一条脱敏案例跑通完整链路：

`raw evidence -> session -> rollout summary -> candidate -> memory-commit -> 最终记忆层`

## 场景

一次已经完成的协作回合里，出现了三类不同信号：

1. 一条可复用的工作记忆路由规则
2. 一条可复用的流程经验
3. 一条不该混进工作记忆的私人成长信号

## 第一步：原始证据

当材料还贴近原始回合、主要价值是用于回溯时，应先放进 `memory-sidecar/`。

示例：

```md
source: conversation
type: evidence

- 用户说 router-first 应该是弱默认，而不是硬前置。
- 用户说 commit 阶段只保留 reject-only 权力。
- 用户指出一条私人成长信号，不该混进工作记忆。
```

## 第二步：session 压缩

session 压缩用于保留本轮可读性，但还不急着把所有内容升级成长久记忆。

示例：

```md
## 2026-04-28

- memory workflow refined
- router-first kept as weak default
- commit-stage authority simplified to reject-only
- one private signal should route to personal memory
```

## 第三步：rollout retrospective

rollout summary 是本轮叙事层，也是第一次说明“为什么这条东西未来可能值得晋升”的地方。

示例：

```md
## Outcome

- work-memory routing became more explicit
- the commit stage stayed thin
- private growth material stayed separate from work memory
```

## 第四步：候选列表

distillation 把 retrospective 转成规范候选。

示例：

```yaml
- candidate_id: C1
  summary: Prefer router-first as a weak narrowing pass for core reads.
  recommended_destination: work_memory
  draft_write: memories/core/runtime_preferences.md

- candidate_id: C2
  summary: Keep commit-stage skills thin and downstream-only.
  recommended_destination: learnings
  draft_write: memories/learnings/LEARNINGS.md

- candidate_id: C3
  summary: A private growth signal is worth keeping, but not in work memory.
  recommended_destination: personal_memory
  draft_write: personal_memory/logs/raw_signals.md
```

## 第五步：reject-only 反馈

用户不需要手动给每条候选指定最终去向。

示例：

```yaml
reject:
  - C2
```

## 第六步：`memory-commit`

`memory-commit` 接收剩余候选，只做最小必要写入。

结果：

- `C1` -> 工作记忆
- `C2` -> reject
- `C3` -> 私人记忆

## 最终落点

- `C1` -> `memories/core/runtime_preferences.md`
- `C2` -> 本轮不入库
- `C3` -> `personal_memory/logs/raw_signals.md`

## 这条链为什么重要

- 原始证据可回溯，但不会过早 durable 化
- rollout retrospective 保留本轮上下文
- distillation 把判断和执行拆开
- reject-only 降低用户审阅成本
- 私人材料可以保留，同时不污染工作记忆
