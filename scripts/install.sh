#!/usr/bin/env bash
# Install one trusted local copy of the prompt-me Agent Skill.
set -euo pipefail

usage() {
  cat <<'HELP'
Usage: bash scripts/install.sh --agent cursor|claude|codex [--scope project|user] [--target PATH] [--dry-run] [--force]

  --agent     Agent for which to install the skill (required)
  --scope     project (default) or user
  --target    Project directory (default: current working directory)
  --dry-run   Show planned action without writing any files
  --force     Back up and replace an existing prompt-me skill directory
  -h, --help  Show this message

No network access is performed. The source is this checkout's skills/prompt-me/.
HELP
}
die() { printf 'ERROR: %s\n' "$*" >&2; exit 2; }

agent=""
scope="project"
target="$PWD"
force=0
dry_run=0
target_specified=0

while (( $# > 0 )); do
  case "$1" in
    --agent) (( $# >= 2 )) || die "--agent requires an argument"; agent="$2"; shift 2 ;;
    --scope) (( $# >= 2 )) || die "--scope requires an argument"; scope="$2"; shift 2 ;;
    --target) (( $# >= 2 )) || die "--target requires an argument"; target="$2"; target_specified=1; shift 2 ;;
    --dry-run) dry_run=1; shift ;;
    --force) force=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) die "Unknown argument: $1" ;;
  esac
done

case "$agent" in
  cursor) dest_root=".cursor/skills" ;;
  claude) dest_root=".claude/skills" ;;
  codex) dest_root=".agents/skills" ;;
  *) die "Choose --agent cursor, claude, or codex" ;;
esac
case "$scope" in
  project)
    [[ -d "$target" ]] || die "Project directory does not exist: $target"
    target="$(cd -- "$target" && pwd -P)"
    ;;
  user)
    (( target_specified == 0 )) || die "--target is only valid with --scope project"
    target="$HOME"
    ;;
  *) die "--scope must be project or user" ;;
esac

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
source_dir="$script_dir/../skills/prompt-me"
[[ -f "$source_dir/SKILL.md" ]] || die "Missing canonical SKILL.md: $source_dir"
destination="$target/$dest_root/prompt-me"
parent_dir="$target/$dest_root"

if [[ -e "$destination" && "$force" -ne 1 ]]; then
  die "Destination exists: $destination (use --force to back up and replace)"
fi

if (( dry_run == 1 )); then
  printf 'DRY RUN: would install %s to %s\n' "$source_dir" "$destination"
  if [[ -e "$destination" ]]; then
    printf 'DRY RUN: would create a timestamped backup of existing destination\n'
  fi
  exit 0
fi

mkdir -p -- "$parent_dir"
temporary="$(mktemp -d "$parent_dir/.prompt-me-install.XXXXXXXX")"
backup=""
cleanup() {
  if [[ -n "$temporary" && -d "$temporary" ]]; then rm -rf -- "$temporary"; fi
}
trap cleanup EXIT
cp -R -- "$source_dir/." "$temporary/"
if [[ -e "$destination" ]]; then
  stamp="$(date -u +%Y%m%dT%H%M%SZ)"
  backup="${destination}.backup.${stamp}.$$"
  mv -- "$destination" "$backup"
fi
if ! mv -- "$temporary" "$destination"; then
  if [[ -n "$backup" && -d "$backup" ]]; then mv -- "$backup" "$destination"; fi
  die "Failed to install; previous version restored when possible"
fi
temporary=""
printf 'Installed prompt-me: %s\n' "$destination"
if [[ -n "$backup" ]]; then printf 'Previous version backed up: %s\n' "$backup"; fi
