#!/bin/sh
set -eu

INPUT="${1:-}"

if [ -n "$INPUT" ]; then
  DATA="$(cat "$INPUT")"
else
  DATA="$(cat)"
fi

require_key() {
  KEY="$1"
  echo "$DATA" | rg -q "^${KEY}:" || {
    echo "missing required key: ${KEY}" >&2
    exit 1
  }
}

require_key "kind"
require_key "intake_id"
require_key "source"
require_key "source_id"
require_key "timestamp"
require_key "write_blocked"

KIND="$(echo "$DATA" | awk -F': ' '/^kind:/{print $2; exit}')"

case "$KIND" in
  route-plan)
    require_key "final_type"
    require_key "template_id"
    require_key "operation"
    require_key "target_note_path"
    ;;
  decision-report)
    require_key "status"
    require_key "agent_read"
    ;;
  *)
    echo "unexpected kind: $KIND" >&2
    exit 1
    ;;
esac

echo "validation ok: $KIND"
