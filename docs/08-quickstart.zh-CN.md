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
- `/tmp/agent-memory/memories/short_term`

## 第二步：校验仓库内样例

```bash
python3 scripts/validate_memory.py --root examples/sanitized-memory --policy checks/policy.json
```

预期输出：`VALIDATION PASSED`

## 第三步：接入你的仓库

1. 复制 `scripts/bootstrap.sh`、`scripts/validate_memory.py`、`checks/policy.json`
2. 配置你自己的 memory root
3. 引入 `.github/workflows/validate-memory.yml`

## 第四步：首次实战

- 在 `core/` 写一条带 frontmatter 的长期规则
- 在 `short_term/session_summaries/` 写一条会话摘要
- 再跑一次校验器

## 故障排查

- 缺 frontmatter：补 `---` 包裹的 YAML 头
- scope 非法：使用 `checks/policy.json` 允许值
- 命中敏感信息检测：先脱敏再提交
