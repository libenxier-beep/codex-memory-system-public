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
require_key "operation"
require_key "result"
require_key "target_note_path"
require_key "template_id"
require_key "write_attempted"

RESULT="$(echo "$DATA" | awk -F': ' '/^result:/{print $2; exit}')"

case "$RESULT" in
  added|updated|skipped|blocked|conflict)
    ;;
  *)
    echo "unexpected result: $RESULT" >&2
    exit 1
    ;;
esac

echo "validation ok: $RESULT"
