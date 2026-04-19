# Codex 长期记忆系统（脱敏版）

这是一个公开的、脱敏后的分层长期记忆系统蓝图，适用于编码代理协作场景。

英文版本请看: [README.md](./README.md)

关键文件中文版统一使用 `*.zh-CN.md` 后缀。

## 这个仓库包含什么

- 分层记忆架构（`core / platform / learnings / short_term`）
- 记忆生命周期（capture -> classify -> deduplicate -> route -> review）
- 加载策略（Ring0-Ring3 渐进加载）
- 记忆写入安全门
- 会后沉淀与历史召回流程
- 从扁平旧文件迁移到分层真源的最小增量模式

## 设计目标

1. 单一真源
2. 低维护成本
3. 高信号、低污染
4. 长期记忆与会话上下文边界明确
5. 结构性改动可审计

## 仓库结构

- `docs/01-architecture.md`：架构总览
- `docs/02-layer-model.md`：分层职责与边界
- `docs/03-memory-lifecycle.md`：写入/更新/复盘生命周期
- `docs/04-routing-and-loading.md`：路由与加载策略
- `docs/05-safety-and-governance.md`：安全与治理规则
- `docs/06-operations-and-audit.md`：运维与审计实践
- `docs/07-migration-pattern.md`：最小增量迁移模式
- `templates/memory-item-template.md`：长期记忆条目模板
- `templates/distillation-report-template.md`：会后沉淀报告模板

## 脱敏策略

本仓库有意移除了以下内容：

- 个人身份信息
- 本地绝对路径
- 访问令牌、凭证与密钥
- 私有项目名称与业务细节

请使用占位符，例如 `$CODEX_HOME`、`PROJECT_ROOT`、`AGENT_HOME`。

## 推荐落地顺序

1. 先读 `docs/01-architecture.md`
2. 套用 `docs/02-layer-model.md`
3. 启用 `docs/05-safety-and-governance.md` 的写入门禁
4. 增加 `docs/06-operations-and-audit.md` 的审计机制
5. 按 `docs/07-migration-pattern.md` 执行迁移检查单

## 许可证

MIT
