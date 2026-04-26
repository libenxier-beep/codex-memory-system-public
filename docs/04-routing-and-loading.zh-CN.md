# 04 路由与加载

## 渐进加载（Ring 模型）

### Ring 0（始终加载）
- memory index
- global principles
- runtime preferences
- 当前平台适配文件

### Ring 1（任务路由）
按任务类型加载 1-2 个相关文件（如 skill 工程、记忆架构、评估、编排等）。

### Ring 2（深度参考）
仅在具体决策需要时加载。
- 只有当任务涉及当前活动、最近 session 状态或原始证据回钻时，才查询 `memory-sidecar/`。

### Ring 3（冷记忆）
仅在显式检索或事故回放时加载。

## 先检索再回答

当用户问历史问题（如“上次”“之前”）时，先召回：

1. 先查整理后的 memory index/summary
2. 再查相关 rollout/session 证据
3. 最后给基于证据的总结回答

## 运行时查询顺序

1. 先看项目内 `docs/progress.md` 的当前 handoff
2. 再看 `memory-sidecar/indexes/` 的 current/recent 入口
3. 不够再读 `memory-sidecar/sessions/` 的压缩上下文
4. 只有确实需要原始证明时才读 `memory-sidecar/evidence/`

## personal_memory 路由规则

- 生活、状态、成长、关系、自我理解类问题，默认优先读 `personal_memory/`
- 只有当用户的问题明确横跨工作决策与个人状态时，才同时读工作记忆和私人记忆
- 私人信号默认不要写进工作向长期记忆，除非用户明确要求做跨域综合

## 路由优先级

1. 范围正确
2. 冲突最小
3. 保护单一真源
4. 维护成本最低
