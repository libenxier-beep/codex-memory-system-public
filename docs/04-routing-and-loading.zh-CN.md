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

### Ring 3（冷记忆）
仅在显式检索或事故回放时加载。

## 先检索再回答

当用户问历史问题（如“上次”“之前”）时，先召回：

1. 先查整理后的 memory index/summary
2. 再查相关 rollout/session 证据
3. 最后给基于证据的总结回答

## 路由优先级

1. 范围正确
2. 冲突最小
3. 保护单一真源
4. 维护成本最低
