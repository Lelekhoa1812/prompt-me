# Example 01 — Refine an ambiguous engineering prompt

> **Fictional example.** No repository has been inspected.

## Input

> Review our backlog and implement all missing features. Make the app production ready and test everything.

## Desired prompt-me outcome

~~~markdown
# Mission: evidence-based backlog reconciliation and delivery planning

You are reviewing an existing application, not starting a new project.

1. Read the authoritative requirements and planning documents available in the current workspace. Follow their documented precedence.
2. Inspect the current implementation, tests, integration points, and actual project state before declaring any feature missing or finished.
3. Build an accessible-requirements coverage matrix: requirement → evidence → status → gap → task → verification.
4. Separate confirmed defects from hypotheses and optional architecture improvements. Do not invent services, files, or technical constraints.
5. Ask me a concise interactive choice question if the approved design or deployment boundary is materially unclear.
6. Produce an atomic execution plan with source references, ownership boundaries, dependencies, acceptance criteria, and failure/regression checks.
7. Do not implement or deploy in this session: this prompt requests an auditable plan only.
8. Finish with the verified baseline, exact unknowns, decisions requiring approval, and first next-agent action.
~~~

## Why this is stronger

It removes silent interpretation of “all”, “ready”, and “everything”; makes scope traceable to actual sources; prevents fabricated test evidence; and distinguishes **writing an implementation plan** from **receiving authority to ship**.
