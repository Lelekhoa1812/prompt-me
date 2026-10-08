# prompt-me

**Turn an imperfect engineering request into an evidence-grounded prompt, an execution-ready plan, and a loss-resistant agent-to-agent handoff.**

[![Validate](https://github.com/Lelekhoa1812/prompt-me/actions/workflows/validate.yml/badge.svg)](https://github.com/Lelekhoa1812/prompt-me/actions/workflows/validate.yml)
![Agent Skills](https://img.shields.io/badge/standard-Agent%20Skills-3159b7)
![Supported](https://img.shields.io/badge/agents-Cursor%20%7C%20Claude%20Code%20%7C%20Codex-333)

**prompt-me** is an instruction-only [Agent Skill](https://agentskills.io/specification) for engineering prompt refinement, repository-aware planning, interactive decision clarification, and traceable A2A handoffs. Its canonical manifest is [skills/prompt-me/SKILL.md](skills/prompt-me/SKILL.md).

> **Status:** Initial repository baseline. Compatibility follows published skill conventions; actual behavior depends on the host agent's mode, permissions, and tools. This repository does not ship an LLM, autonomous orchestrator, or production deployment service.

## Why it exists

Engineering prompts often leave critical details implicit: which decisions were already agreed, whether features are shipped, what branch is authoritative, which facts are verified, which design questions require approval, and what proves completion. The result is agent drift, speculative plans, incomplete tests, and fragile handoffs.

prompt-me turns these loosely specified requests into **traceable execution contracts**. It avoids promising impossible 100% context coverage; instead, it maps all **accessible** requirements and evidence and visibly marks missing context. See [Problem statement](docs/PROBLEM.md).

## What it does

| Capability | Expected outcome |
| --- | --- |
| Intent preservation | Carries original goals, constraints, named systems, and delivery mode forward without inventing requirements |
| Adaptive project reconnaissance | Skims relevant repository material when accessible; deepens only where evidence is needed |
| Interactive decision gates | Prefers a host's supported question UI for consequential choices, with a concise chat fallback |
| High-fidelity prompt rewriting | Produces ready-to-paste prompts with explicit first actions, scope, guardrails, and evidence rules |
| Atomic execution planning | Provides task/requirement/verification traceability when a plan is requested |
| Agent-to-agent (A2A) handoff | Specifies task input and result transcripts that carry decisions, dependencies, evidence, and continuation state |
| Delivery validation | Specifies observable acceptance criteria and live-app/regression checks for downstream implementation work |

**Not its default job:** autonomously changing application code, merging branches, deploying software, fabricating project context, or bypassing required approvals. Those require an independently authorised execution task.

## Quick start

Clone the repository, then install the skill into the project where your coding agent will work:

~~~bash
git clone https://github.com/Lelekhoa1812/prompt-me.git
cd prompt-me

# Example: install for Cursor into a different local project
bash scripts/install.sh --agent cursor --scope project --target /path/to/your-project

# Alternatives
bash scripts/install.sh --agent claude --scope project --target /path/to/your-project
bash scripts/install.sh --agent codex  --scope project --target /path/to/your-project
~~~

To install globally for your user, replace `--scope project --target ...` with `--scope user`. The installer refuses overwrites unless `--force` is provided; use `--dry-run` to preview. See the [complete installation guide](docs/INSTALLATION.md).

### Start using the skill

In your agent chat:

> Use the prompt-me skill to refine the following request into a ready-to-paste execution prompt. Inspect the relevant project docs first, preserve existing decisions, and ask me concise interactive questions only for unresolved high-impact choices: [paste request]

For a broader handoff:

> Use prompt-me to review this plan against the actual repository, identify unverified gaps, and deliver a requirement-linked atomic execution plan and A2A handoffs. Do not implement application changes; I am asking for a plan.

See [examples](examples/) for prompt improvement, branch reconciliation, post-merge hardening, and a sample handoff.

## Documentation

| Start here | Purpose |
| --- | --- |
| [Problem & design goals](docs/PROBLEM.md) | The failure modes the skill is designed to address |
| [How it works](docs/HOW-IT-WORKS.md) | Modes, context acquisition, decision gates, outputs |
| [Install & update](docs/INSTALLATION.md) | Local/global installs, safety, uninstall |
| [Agent compatibility](docs/COMPATIBILITY.md) | Cursor, Claude Code, Codex, native question-tool caveats |
| [A2A contract](docs/A2A-PROTOCOL.md) | Input/output schemas and provenance |
| [Quality & safety](docs/QUALITY-AND-SAFETY.md) | Evidence, hallucination controls, testing, authorisation |
| [Troubleshooting & FAQ](docs/FAQ.md) | Typical installation and behavior failures |
| [Development roadmap](docs/ROADMAP.md) | Future directions, explicitly not shipped features |
| [Contributing](CONTRIBUTING.md) | How to propose changes safely |

## Repository structure

~~~text
skills/prompt-me/SKILL.md      Canonical, portable skill instructions
docs/                          Purpose, installation, protocols, quality
examples/                      Illustrative inputs, decisions, and handoffs
scripts/install.sh             Explicit, non-destructive installer
scripts/validate.py            Skill/package validation
tests/                         Automated validator/installer tests
.github/                       CI and contribution templates
~~~

## Design principles

**Evidence > assertion · Intent > rewriting style · Interactivity > questionnaires · Verification > confidence · Handoff completeness > chat memory · Safety > silent autonomy.**

## Project and legal status

This is an independently maintained community project, **not affiliated with or endorsed by Microsoft, Cursor, Anthropic, or OpenAI**. 

**License:** No license has been selected by the repository owner yet. Public visibility is not itself permission to redistribute or modify. See [contribution guidance](CONTRIBUTING.md) until a license is chosen.

For vulnerability reports, use [SECURITY.md](SECURITY.md). For usage questions, see [SUPPORT.md](SUPPORT.md).
