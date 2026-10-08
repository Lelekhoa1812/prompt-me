# Problem statement and goals

## Problem

Coding agents can execute impressive amounts of work but lose quality when a user hands over an ambiguous brief, stale plan, or long-running project's context. Common failure modes include:

1. **Requirement drift:** a well-meaning rewrite silently changes intent or adds features.
2. **Context gaps:** the agent guesses at files, decisions, state, contracts, or implementation status instead of inspecting accessible evidence.
3. **Unusable clarification:** material design decisions arrive as multi-page audits or questionnaires rather than concise, actionable choices.
4. **Non-atomic plans:** tasks lack dependencies, ownership boundaries, acceptance criteria, or reproduction steps.
5. **A2A context loss:** downstream agents inherit a summary, but not the decisions, evidence, constraints, or exact continuation point.
6. **False completion:** “done” means code written or tests green, while integrated app behavior remains unverified.
7. **Unsafe autonomy:** branch changes, credential use, production mutations, or high-risk architecture choices are silently assumed.

## The intended intervention

prompt-me is a **meta-skill** that teaches a capable host agent to produce faithful, evidence-grounded prompts and handoff-ready plans. When it has relevant project access, it may perform bounded, read-only reconnaissance and appropriately authorised non-destructive checks. The resulting instructions explicitly separate facts, uncertainty, proposals, and approval gates.

It **does not implement a separate orchestration engine**, guarantee the host agent has tools, automatically retrieve inaccessible history, or replace the host's security controls.

## Users

- Engineers handing off work to Cursor, Claude Code, or Codex.
- Engineering leads reviewing weak implementation plans or partially shipped systems.
- Teams coordinating parallel agents across tasks, branches, and design decisions.
- Contributors creating auditable prompts instead of relying on a single chat session's memory.

## Success criteria

A successful skill invocation produces a deliverable that:

- Preserves all explicitly stated goals, constraints, non-goals, and current-state claims.
- Grounds project-specific assertions in inspectable sources or marks them unverified.
- Uses concise interactive clarification only for genuinely consequential open decisions.
- Clearly distinguishes **refinement only** from **authorised execution**.
- Maps relevant requirements to concrete tasks, dependencies, tests, and completion evidence when planning is requested.
- Enables a fresh agent to continue work without relying on unrecorded conversation context.
- Records limitations rather than claiming perfect coverage or completed tests it did not run.

## Non-goals

- Literal 100% context completeness despite missing data or permissions.
- Guaranteed equivalence of Cursor, Claude Code, and Codex UIs.
- Unprompted code modifications, merges, or deployments.
- Automatic approval of major architecture or product-scope decisions.
- Substituting formal compliance certification, product QA, or security review.

## Boundaries

Each target project retains its own authoritative requirements and decision precedence. The skill supplies a **method of working**, never universal project architecture. Examples in this repository are hypothetical teaching artefacts, not statements about the user's application.
