# 09 执行技能

## 目的

这个仓库把记忆架构和执行技能分开描述，但真正让架构在实战里可用的核心技能主要有两个：

- `post-collaboration-distillation`
- `memory-commit`

它们组成默认的任务后记忆维护主链路。

## 默认链路

1. 主任务完成
2. `post-collaboration-distillation` 审视本轮协作
3. 产出候选列表
4. 用户通过 reject-only 方式筛掉不接受的候选
5. `memory-commit` 把剩余批准结果写入正确层级

## `post-collaboration-distillation`

当主要问题是：一轮完成后的任务里，到底什么值得记住，应该先用这个技能。

它应该负责：

- 总结这轮完成了什么，以及真正重要的变化
- 剔除低信号、局部性强、不可复用的噪音
- 对照现有记忆做去重、合并、升级、拆分或丢弃判断
- 决定候选应该去 sidecar、rollout retrospectives、工作记忆、私人记忆，还是根本不该入库
- 输出结构化 Distillation Report

它不应该负责：

- 取代原始任务本身
- 从弱证据里硬造长期结论
- 跳过去重和范围检查直接写库

## `memory-commit`

只有在 distillation 已经完成、而且已经存在一份规范候选列表时，才使用这个技能。

它应该负责：

- 规范化 reject-only 用户反馈
- 默认把未被拒绝的候选视为接受
- 把接受项路由到 `rollout_summaries/`、工作记忆或 `personal_memory/`
- 只做最小必要写入
- 输出 Commit Report

它不应该负责：

- 从原始聊天重新开始做 distillation
- 重新给候选打分或重排优先级
- 绕开现有真源文件自行定义路由规则

## 两者关系

- `post-collaboration-distillation` 解决的是：什么值得保留？
- `memory-commit` 解决的是：接受的内容最终该落到哪里，要改哪些文件？

把两者拆开，可以减少误入长期层的风险，也能降低用户审阅成本。

## 邻接技能：`forge`

`forge` 依然有价值，但它不属于默认的任务后记忆维护主链路。

当主要任务是直接从外部文章、笔记、框架或工作流材料中学习，并把这些材料转成长期升级时，再用 `forge`。

## 相关模板

- `templates/distillation-report-template.md`
- `templates/commit-report-template.md`
