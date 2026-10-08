#!/usr/bin/env bash
set -euo pipefail
repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
tmp_dir="$(mktemp -d)"
trap 'rm -rf -- "$tmp_dir"' EXIT
mkdir -p "$tmp_dir/app"
bash "$repo_dir/scripts/install.sh" --agent cursor --target "$tmp_dir/app" --dry-run
[[ ! -e "$tmp_dir/app/.cursor/skills/prompt-me" ]]
bash "$repo_dir/scripts/install.sh" --agent cursor --target "$tmp_dir/app"
cmp "$repo_dir/skills/prompt-me/SKILL.md" "$tmp_dir/app/.cursor/skills/prompt-me/SKILL.md"
if bash "$repo_dir/scripts/install.sh" --agent cursor --target "$tmp_dir/app" 2>/dev/null; then
  echo "Installer incorrectly overwrote existing destination" >&2; exit 1
fi
bash "$repo_dir/scripts/install.sh" --agent cursor --target "$tmp_dir/app" --force
cmp "$repo_dir/skills/prompt-me/SKILL.md" "$tmp_dir/app/.cursor/skills/prompt-me/SKILL.md"
compgen -G "$tmp_dir/app/.cursor/skills/prompt-me.backup.*" >/dev/null
bash "$repo_dir/scripts/install.sh" --agent claude --target "$tmp_dir/app"
[[ -f "$tmp_dir/app/.claude/skills/prompt-me/SKILL.md" ]]
bash "$repo_dir/scripts/install.sh" --agent codex --scope user --dry-run
echo "PASS: installer safety, dry-run, force/backup, and agent destinations"
