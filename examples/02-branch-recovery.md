# Example 02 — Recover interrupted branch work

> **Fictional scenario.** Several agents worked on separate branches; their cloud sessions are no longer available.

## Input

> We are on main. Explore all branches, decide what can merge, preserve decisions, and continue anything unfinished.

## Refined investigation and execution contract

~~~markdown
# Mission: branch recovery and integration analysis

Current state to verify: local main may differ from remote main; side branches may be incomplete.

Phase 1 — Safe Git baseline: inspect working tree, branches, relevant remote refs, merge bases, and accessible worktrees. Never reset or overwrite unknown work.

Phase 2 — Parallel evidence gathering: investigate independent branches when supported. For each branch capture goal, actual changed files, unique commits, feature behavior, confirmed decisions, missing tasks, conflicts and tests.

Phase 3 — Cross-branch reconciliation: compare semantic behavior and architecture, not only Git conflicts. Give each change set a justified disposition: ready / remediation / continue / reconcile / redundant / blocked.

Phase 4 — Interactive design gate: ask the user concise, evidence-based choices only for unresolved consequential conflicts. Don't assume approval.

Phase 5 — Atomic A2A handoffs: issue stable task IDs, verified starting baselines, actual files, dependencies, locked decisions, acceptance scenarios, integration checkpoints, and honest status.

Phase 6 — If explicitly authorised to implement: finish remaining tasks on safe branches, verify affected app paths, and integrate only after tests and approval gates. Otherwise output the plan and stop.
~~~

## Special cautions

Cloud agent work that was never committed or transferred may be inaccessible; label that limitation. A Git merge without conflicts does not demonstrate that the feature meets behavioral requirements.
