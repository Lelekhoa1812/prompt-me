# Example 03 — Post-merge hardening and delivery

> **Fictional scenario.** Previously separate features were already integrated; the current plan is superficial.

## Input

> The branch reconciliation is shipped. Challenge our weak remaining plan, find live-app defects, fully decompose work, and hand off everything to implementation agents.

## Refined prompt excerpt

~~~markdown
# Mission: harden the current integrated system

The prior cross-branch reconciliation is already complete. DO NOT restart branch recovery unless the current Git state provides contrary evidence.

1. Establish the current authoritative main and preserve any dirty worktree.
2. Compare the existing plan against accessible authoritative requirements, accepted decisions, implementation, and tests.
3. In an approved safe environment, exercise representative app journeys. Separate observed runtime failures, static-code risks, and unverified hypotheses.
4. Review relevant subsystems grounded in the repository, such as harness, orchestration, context propagation, conflict handling, durable execution, code review, and integration boundaries — only if present or in scope.
5. For each gap: capture expected/actual behavior, reproduction, evidence, affected contract, dependencies, remediation, negative/regression tests, and live verification requirements.
6. Replace vague epics with atomic, independently assignable implementation tasks and A2A input/output contracts.
7. Before consequential architecture or scope changes, ask the user a focused native choice question if supported.
8. The receiving engineer is authorised to implement only tasks approved in the resulting plan, within the available environment and operational permissions.
9. Record precisely which tasks were only planned, implemented, tested, verified, or integrated. If blocked, preserve an exact continuation handoff.
~~~

## Why this matters

It treats “already shipped” as **current-state input to verify**, avoids redundant branch forensics, and uses observed behavior to drive plan changes instead of expanding an untested document.
