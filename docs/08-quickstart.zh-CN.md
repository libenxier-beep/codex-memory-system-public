# 08 快速开始（15 分钟）

## 目标

快速得到一套可运行的记忆机制：脚手架 + 校验 + CI。

## 前置条件

- bash
- python3
- git

## 第一步：初始化分层记忆目录

```bash
bash scripts/bootstrap.sh /tmp/agent-memory
```

预期结果：

- `/tmp/agent-memory/memories/core`
- `/tmp/agent-memory/memories/platform`
- `/tmp/agent-memory/memories/learnings`
- `/tmp/agent-memory/memories/rollout_summaries`
- `/tmp/agent-memory/memory-sidecar/evidence`
- `/tmp/agent-memory/memory-sidecar/sessions`
- `/tmp/agent-memory/memory-sidecar/indexes`

## 第二步：校验仓库内样例

```bash
python3 scripts/validate_memory.py --root examples/sanitized-memory --policy checks/policy.json
```

预期输出：`VALIDATION PASSED`

你也可以直接校验刚刚 bootstrap 出来的真实目录：

```bash
python3 scripts/validate_memory.py --root /tmp/agent-memory --policy checks/policy.json
```

预期结果：

- `memories/core`、`memories/platform`、`memories/learnings` 下的长期文件能通过 frontmatter 检查
- `memories/` 与 `memory-sidecar/` 的目录结构符合 target-root 约定
- `memory_index.md` 引用、长期条目 `id` 唯一性、`status`、`last_reviewed`、`supersedes` 也能通过校验

## 第三步：运行 validator 回归夹具

```bash
python3 tests/run_validator_fixtures.py
```

预期结果：

- `valid` 夹具通过
- 负向夹具只因为预期原因失败
- policy 或 validator 改动引入回归时，CI 能及时拦下

## 第四步：接入你的仓库

1. 复制 `scripts/bootstrap.sh`、`scripts/validate_memory.py`、`checks/policy.json`
2. 配置你自己的 memory root
3. 引入 `.github/workflows/validate-memory.yml`

## 第五步：首次实战

- 在 `memories/core/` 写一条带 frontmatter 的长期规则
- 在 `memory-sidecar/sessions/` 写一条运行时 session 摘要
- 在真实项目里，把当前回合 handoff 写进 `PROJECT_ROOT/docs/progress.md`
- 如果需要私人长期理解，再额外建立 `personal_memory/logs/raw_signals.md` 和 `personal_memory/logs/growth_log.md` 作为独立支线
- 再跑一次校验器

## 故障排查

- 缺 frontmatter：补 `---` 包裹的 YAML 头
- layer 或 scope 非法：使用 `checks/policy.json` 允许值
- status 或日期非法：使用 `checks/policy.json` 的枚举值，并把日期写成 ISO 格式
- `supersedes` 断链：引用已有 memory `id`，不要写文件路径
- 命中敏感信息检测：先脱敏再提交
