# Codex 长期记忆系统（脱敏版）

这是一个公开的、脱敏后的分层长期记忆系统蓝图，适用于编码代理协作场景。

英文版本请看: [README.md](./README.md)

关键文件中文版统一使用 `*.zh-CN.md` 后缀。

## 系统流程图

```mermaid
flowchart LR
    A["工作 / 对话 / 反思输入"] --> B["项目 handoff<br/>PROJECT_ROOT/docs/progress.md"]
    A --> C["原始证据<br/>memory-sidecar/evidence"]
    A --> P["个人信号识别"]

    C --> D["Session 压缩<br/>memory-sidecar/sessions"]
    D --> E["轻索引<br/>memory-sidecar/indexes"]
    D --> F["完整回合复盘<br/>memories/rollout_summaries"]

    F --> G{"晋升判断"}

    G --> H["core<br/>长期协作规则"]
    G --> I["platform<br/>平台适配规则"]
    G --> J["learnings<br/>复用经验"]
    G --> K["personal_memory<br/>私人长期理解"]

    P --> K

    L["当前 / 最近查询"] --> B
    L --> E
    L --> D
    L --> C

    M["历史召回"] --> F
    M --> H
    M --> I
    M --> J
    M --> K
```

## 这个仓库包含什么

- 分层记忆架构（`core / platform / learnings / rollout_summaries`）
- 记忆生命周期（capture -> classify -> deduplicate -> route -> review）
- 加载策略（Ring0-Ring3 渐进加载）
- 记忆写入安全门
- 会后沉淀与历史召回流程
- 可选的运行时 sidecar（`memory-sidecar/`），用于 evidence、sessions 与轻索引
- 可选的私人 `personal_memory/` 支线，用于成长信号、私人模式和长期自我理解
- 从扁平旧文件迁移到分层真源的最小增量模式
- 可执行的一键初始化脚本
- 可落地的校验器与 CI 质量门禁
- 可直接跑通的脱敏样例

## 设计目标

1. 单一真源
2. 低维护成本
3. 高信号、低污染
4. 长期记忆、复盘层、运行时上下文、私人记忆边界明确
5. 结构性改动可审计

## 仓库结构

- `docs/01-architecture.md`：架构总览
- `docs/02-layer-model.md`：分层职责与边界
- `docs/03-memory-lifecycle.md`：写入/更新/复盘生命周期
- `docs/04-routing-and-loading.md`：路由与加载策略
- `docs/05-safety-and-governance.md`：安全与治理规则
- `docs/06-operations-and-audit.md`：运维与审计实践
- `docs/07-migration-pattern.md`：最小增量迁移模式
- `docs/08-quickstart.md`：15 分钟可执行上手
- `templates/memory-item-template.md`：长期记忆条目模板
- `templates/distillation-report-template.md`：会后沉淀报告模板
- `scripts/bootstrap.sh`：一键初始化分层记忆目录
- `scripts/validate_memory.py`：schema 与安全规则校验器
- `checks/policy.json`：校验策略契约
- `.github/workflows/validate-memory.yml`：PR 与主干自动校验
- `examples/sanitized-memory/`：可运行脱敏样例

## 快速开始

```bash
bash scripts/bootstrap.sh /tmp/agent-memory
python3 scripts/validate_memory.py --root examples/sanitized-memory --policy checks/policy.json
```

完整步骤见 `docs/08-quickstart.md`。

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
6. 建议让你自己的 Agent 把旧的平铺记忆文件迁移到这套分层结构；只有在确实需要运行时证据召回时，再额外接入 `memory-sidecar/`。
7. 如果你需要私人长期成长支线，再单独接入 `personal_memory/`，不要默认和工作记忆混层。

## 许可证

MIT
