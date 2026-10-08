# Agent compatibility and limitations

The manifest uses the portable `SKILL.md` + YAML frontmatter convention. This is **format compatibility**, not a claim that all host models expose the same tools or behave identically.

| Capability | Cursor | Claude Code | Codex |
| --- | --- | --- | --- |
| Portable `SKILL.md` | Supported by published skills convention | Supported by published skills convention | Supported by published Agent Skills conventions |
| Typical project install | `.cursor/skills/prompt-me/` | `.claude/skills/prompt-me/` | `.agents/skills/prompt-me/` |
| Typical user install | `~/.cursor/skills/prompt-me/` | `~/.claude/skills/prompt-me/` | `~/.agents/skills/prompt-me/` |
| Interactive question tool | Prefer `AskQuestion` *if exposed* | Prefer `AskUserQuestion` *if exposed* | Prefer `request_user_input` or actual exposed equivalent |
| Native question UI guaranteed? | No | No | No |
| Parallel sub-agents guaranteed? | No | No | No |
| Live-project or filesystem access guaranteed? | No | No | No |

## Native decision tools

The instruction is to **use the platform's real interactive question-selection tool** when available, *not* to merely mention the tool name or emit a fake invocation. A tool's availability can depend on model, mode, version, and deployment.

If no supported question tool is exposed, ask one focused choice-based question **inline in chat**. Never suppress an approval gate because the preferred UI is absent.

Do not substitute a complete technical report for a narrow product decision. Conversely, do not ask the user to approve low-risk implementation mechanics already determined by authoritative project guidance.

## Invocation examples

- Cursor: “Use prompt-me to refine this branch recovery brief before implementation.”
- Claude Code: “/prompt-me Improve this engineering handoff; clarify any consequential decision with me.”
- Codex: “Use the prompt-me skill to harden this plan and produce atomic A2A tasks.”

The exact automatic/explicit invocation flow may differ with the installed agent.

## What this does not promise

- Identical invocation syntax or tool call names across platforms.
- Agent-to-agent communication infrastructure (the protocol is a textual contract).
- Automatic sharing of user-level skills to cloud agents; check the host's sync and workspace rules.
- Stable availability of planning modes, code editors, browsers, CI, credentials, or Git remotes.
- Access to prior cloud-agent transcripts not present in the current workspace.

## Compatibility maintenance

When vendors change skill discovery or question interfaces, raise a documentation issue with: client/version, mode, observed behavior, source link, and a minimal reproduction. Update the documentation and tests before claiming expanded support.
