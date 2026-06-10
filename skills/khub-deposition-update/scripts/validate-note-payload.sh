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
require_key "final_type"
require_key "template_id"
require_key "target_note_title"
require_key "target_note_path"
require_key "frontmatter"
require_key "sections"

KIND="$(echo "$DATA" | awk -F': ' '/^kind:/{print $2; exit}')"

if [ "$KIND" != "note-payload" ]; then
  echo "unexpected kind: $KIND" >&2
  exit 1
fi

echo "validation ok: note-payload"
