kind: decision-report
intake_id: MjMxYYYYYY
status: needs_human_decision
source: flomo
source_id: MjMxYYYYYY
timestamp: 2026-04-14 20:06
raw_link: https://flomoapp.com/...
raw_text: 这条内容既像认知框架，也像一个可执行流程卡。
agent_read: The note can plausibly become either a cognition or a playbook, and the current evidence is not strong enough to choose automatically.
best_candidates:
  - final_type: cognition
    target_area: 25_Personal_Growth
    confidence: 0.52
    why_not: Workflow structure is unusually strong.
  - final_type: playbook
    target_area: 25_Personal_Growth
    confidence: 0.49
    why_not: Judgment layer is unusually strong.
why_not_fit:
  - ambiguous_type_choice
suggested_next_decisions:
  - choose_cognition
  - choose_playbook
  - split_into_two_notes
write_blocked: true
