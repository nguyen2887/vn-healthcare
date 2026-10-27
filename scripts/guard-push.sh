#!/usr/bin/env bash
# PreToolUse(Bash) hook: contributor không được push/commit thẳng lên main. Rào mềm.
cd "$(dirname "$0")/.." || exit 0
[ -f .owner ] && exit 0
cmd=$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null)
if echo "$cmd" | grep -Eq 'git +push[^|;&]*\b(main|master)\b|git +push +(-f|--force)'; then
  echo "Contributor không push thẳng main/master. Tạo nhánh field/<tên>-<chủ đề> rồi mở PR." >&2
  exit 2
fi
branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
if [ "$branch" = "main" ] && echo "$cmd" | grep -Eq 'git +commit'; then
  echo "Đang ở main. Contributor commit trên nhánh riêng: git checkout -b field/<tên>-<chủ đề>" >&2
  exit 2
fi
exit 0
