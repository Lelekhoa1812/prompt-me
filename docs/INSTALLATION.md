# Install, verify, update, and uninstall

## Prerequisites

- Git and a shell for the scripted workflow; manual installation only needs a file manager.
- An agent supporting the [Agent Skills format](https://agentskills.io/specification).
- A **trusted project** and read permission to the skill files.

No external runtime or language package is needed to **use** the skill: it consists of instructions, not executable agent code.

## Repository checkout

~~~bash
git clone https://github.com/Lelekhoa1812/prompt-me.git
cd prompt-me
~~~

## Installer (recommended)

Run from the cloned repository. The installer **copies** the canonical skill directory; it does not modify the target application's code or install third-party packages.

~~~bash
bash scripts/install.sh --agent cursor --scope project --target /path/to/project
bash scripts/install.sh --agent claude --scope project --target /path/to/project
bash scripts/install.sh --agent codex  --scope project --target /path/to/project
~~~

Use `--scope user` for a user-wide installation (no `--target` needed). Use `--dry-run` before writing; `--force` replaces only the selected destination skill directory, after a backup is made by the installer.

| Agent | Project scope | User scope |
| --- | --- | --- |
| Cursor | `.cursor/skills/prompt-me/` | `~/.cursor/skills/prompt-me/` |
| Claude Code | `.claude/skills/prompt-me/` | `~/.claude/skills/prompt-me/` |
| Codex | `.agents/skills/prompt-me/` | `~/.agents/skills/prompt-me/` |

**Shared installs:** Cursor also discovers `.agents/skills/` and other compatible locations in many environments. If you install in multiple locations, avoid conflicting copies of the same skill; keep all copies in sync.

## Manual installation

Copy the directory `skills/prompt-me/` into the selected path above so the final file is `<skill-root>/prompt-me/SKILL.md` (not `skills/prompt-me/SKILL.md` under the target root).

Example:

~~~bash
mkdir -p /path/to/project/.cursor/skills/prompt-me
cp skills/prompt-me/SKILL.md /path/to/project/.cursor/skills/prompt-me/SKILL.md
~~~

## Verify discovery

Open or restart your agent session, use its skill view/command discovery if available, then ask:

> Use prompt-me to refine this request without inventing project facts: “Check our work and ship everything.”

Confirm it returns a structured refined prompt instead of claiming it has already shipped. UI invocation varies by agent/version.

## Update

From your checkout:

~~~bash
git pull --ff-only
bash scripts/install.sh --agent cursor --scope project --target /path/to/project --force
~~~

The installer creates a timestamped backup before replacing the existing skill folder. Repeat for the agent(s) you use.

## Uninstall

Manually delete **only the installed `prompt-me` skill directory** under the selected agent's skills folder. Removing the source repository does not necessarily remove any installed copies.

## Security notes

Inspect skill instructions before installation. This is a prompt workflow; its behavior inherits the active agent's permissions, model, workspace trust, tools, and policies. Do not execute remote shell downloads blindly. For safe handling of source material, see [Quality & safety](QUALITY-AND-SAFETY.md).

## Authoritative references

- [Agent Skills specification](https://agentskills.io/specification)
- [Cursor Agent Skills](https://cursor.com/docs/skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [OpenAI skills documentation](https://developers.openai.com/api/docs/guides/tools-skills)

Agent product behavior evolves; consult vendor documentation when a path or capability changes.
