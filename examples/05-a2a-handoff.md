# Example 05 — Concrete A2A handoff with honest unknowns

> **Fictional example:** this is a demonstration of format and status discipline, not a claim about an actual codebase.

## Input packet

~~~yaml
handoff_type: input
task_id: TASK-017
mission: "Recover a task after worker interruption without duplicate processing."
requirement_ids: ["REQ-RECOVERY-02 (hypothetical)"]
authority:
  sources: ["TO INVESTIGATE: find governing runtime specification"]
baseline:
  branch: "TO INVESTIGATE: inspect actual checkout"
  commit: "TO INVESTIGATE: capture git HEAD"
current_state:
  verified: []
  unknown: ["checkpoint format", "task acknowledgement semantics"]
locked_decisions: []
non_goals: ["Do not change unrelated task scheduling behavior."]
scope:
  relevant_files: ["TO INVESTIGATE: find worker persistence and recovery paths"]
  edit_boundaries: ["Do not edit until ownership is assigned."]
dependencies: ["Confirm actual persistence contract."]
implementation: ["Trace interruption and resumption flow", "Propose fix based on observed bug"]
acceptance_criteria:
  - "An interrupted task resumes or terminates according to the confirmed requirement."
  - "No duplicate side effects in the approved test fixture."
verification:
  - "Run an authorised interruption/restart scenario with tracked task identifiers."
approvals_required:
  - "Confirm recovery semantics if authoritative sources conflict."
continuation_context: "Do not assume the runtime is idempotent."
~~~

## Output packet (investigation-only)

~~~yaml
handoff_type: output
task_id: TASK-017
status: investigated
baseline_revision: "UNKNOWN: no repository access in this fictional example"
resulting_revision: null
changes:
  files: []
  contracts: []
  behavior: []
decisions:
  applied: []
  deviations: []
verification:
  tests:
    - command_or_scenario: "Worker interruption test"
      expected: "Recovery consistent with approved requirement"
      actual: "not-run; no accessible environment"
      status: not-run
  live_app:
    environment: "unavailable in example"
    observed: "not-run"
defects:
  fixed: []
  open: ["Task recovery behavior has not been observed or diagnosed."]
dependency_impact: ["Unable to assess until code inspection."]
acceptance_evidence: []
blockers: ["Missing authoritative specification and repository access."]
next_action: "Locate requirement and implementation, reproduce an interruption, then update this task."
~~~

### Contract takeaway

The output is valuable **because it does not pretend to have shipped or tested anything**. A new agent knows exactly what must be discovered and which assertions cannot yet be trusted.
