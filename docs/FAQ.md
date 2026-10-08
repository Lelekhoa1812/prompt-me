# Frequently asked questions & troubleshooting

### Is prompt-me an LLM or autonomous multi-agent runtime?

No. It is an **instruction skill** loaded by a compatible host agent. The host determines tools, reasoning capacity, code access, and execution permissions.

### Does it actually inspect my repository?

Only when the host has access, the request benefits from inspection, and the operation is authorised. Otherwise it writes conditional investigation steps and labels unverified facts.

### Can it guarantee 100% project context?

No. It aims for **auditable coverage of accessible sources** and flags missing evidence. Claiming total coverage of unseen history would violate the skill's own rules.

### Will it use AskQuestion, AskUserQuestion, or request_user_input?

It prefers the real native decision UI **if that tool is present**. If not, it asks a compact choice-based question inline. Tool availability depends on agent, model and mode.

### Will it make my agents start implementing immediately?

Not by default. A request to refine a prompt produces a prompt. If you explicitly instruct the current agent to build or modify code, the host must still follow its own permissions and safety gates.

### How do I install in a project?

See [Installation](INSTALLATION.md). The `SKILL.md` must be inside a folder named `prompt-me` under the client’s supported skill root.

### The skill doesn't appear

Check the exact file path and frontmatter, restart/reload the session, inspect the host skill UI and project trust settings, and confirm you installed in the correct working project. User-level cloud sync may differ. Try explicitly asking to use `prompt-me`.

### My agent ignored the question tool

Check whether the actual tool is exposed in the current mode. The skill cannot force an unavailable tool; inline questions are the safe fallback.

### My handoff is vague

Ask for an evidence-linked task input/output envelope using the [A2A contract](A2A-PROTOCOL.md), including acceptance criteria, exact source references, test outcomes, and continuation point.

### My agent invented project files or architecture

Stop the affected plan or execution; ask it to mark unsupported claims `Unknown` or `TO INVESTIGATE` and verify against accessible sources. File an issue with a sanitized reproduction.

### Do I need to install anything from pip or npm?

Not to **use** the skill. Development validation may use Python tooling as documented in [CONTRIBUTING](../CONTRIBUTING.md).

### May I reuse and redistribute the project?

A license has not yet been selected. Please do not infer redistribution permission from a public GitHub repository. Check its latest license status.
