# Agent-to-agent handoff protocol

**Purpose:** a handoff is an independently actionable and auditable task contract, not a broad summary and not evidence of completed work. The canonical field definitions live in [SKILL.md](../skills/prompt-me/SKILL.md).

## Operating rules

1. **Stable identity:** Keep one TASK-ID from planning through verification. Do not recycle IDs.
2. **Provenance:** Distinguish user requirements, repository evidence, observed behavior, hypotheses, and recommendations.
3. **Version-aware:** Include a branch/revision only when actually known; otherwise specify how to establish it.
4. **Authority:** Explicitly preserve accepted decisions, exclusions, and approval gates.
5. **Isolation:** Specify owner, editable boundary, overlapping work, and upstream/downstream dependencies.
6. **Falsifiability:** State exact acceptance conditions and tests, not just “works.”
7. **Truthful status:** `implemented`, `tested`, `verified`, and `integrated` are different states.
8. **No hidden chat dependencies:** A fresh recipient must receive the context required to resume independently.
9. **No imaginary data:** For unknown files, interfaces, commands, or environment, specify `TO INVESTIGATE` and a discovery step.

## Task input envelope

~~~yaml
handoff_type: input
task_id: TASK-001
mission: "[observable result]"
requirement_ids: ["[source-linked IDs]"]
authority:
  sources: ["[real files/docs and precedence]"]
baseline:
  branch: "[known branch or TO INVESTIGATE]"
  commit: "[known revision or TO INVESTIGATE]"
current_state:
  verified: ["[observed fact and evidence]"]
  unknown: ["[unverified assumptions]"]
locked_decisions: ["[approved decisions]"]
non_goals: ["[explicit exclusions]"]
scope:
  relevant_files: ["[verified paths]"]
  edit_boundaries: ["[allowed components]"]
dependencies: ["[other tasks or contracts]"]
implementation: ["[detailed technical steps]"]
acceptance_criteria: ["[observable condition]"]
verification: ["[test, expected result, and environment]"]
approvals_required: ["[consequential decisions only]"]
continuation_context: "[what the next agent must not rediscover]"
~~~

## Execution output transcript

~~~yaml
handoff_type: output
task_id: TASK-001
status: "[investigated|planned|implemented|tested|verified|integrated|blocked]"
baseline_revision: "[actual revision]"
resulting_revision: "[actual revision, if changed]"
changes:
  files: ["[actual files]"]
  contracts: ["[interface or schema changes]"]
  behavior: ["[observable change]"]
decisions:
  applied: ["[decision ID and rationale]"]
  deviations: ["[new approvals or unresolved conflict]"]
verification:
  tests:
    - command_or_scenario: "[actual command or scenario]"
      expected: "[expected result]"
      actual: "[observed result]"
      status: "[pass|fail|blocked|not-run]"
  live_app:
    environment: "[actual environment or unavailable]"
    observed: "[actual result or not-run]"
defects:
  fixed: ["[with evidence]"]
  open: ["[reproduction and impact]"]
dependency_impact: ["[downstream effects]"]
acceptance_evidence: ["[logs/diffs/traces/references]"]
blockers: ["[precise unmet requirements]"]
next_action: "[exact continuation point and prerequisite]"
~~~

The fields above are **templates**, not invented information about a real repository. Use real IDs and source locations in actual handoffs.

## Coordinator validation

A parent/coordinating agent must check critical downstream claims against actual code, logs, tests, and repository state. Do not infer “merged” from “implemented” or “live validated” from “unit-tested.”

## Example

See [a worked transcript](../examples/05-a2a-handoff.md) illustrating missing context and honest `not-run` test status.
