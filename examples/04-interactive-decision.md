# Example 04 — Early interactive decision

> **Fictional example:** two authoritative sources disagree on the expected retry behavior.

## Bad approach

Write a long report with ten architecture options and bury a request for approval near the end. Or silently choose a retry policy without evidence.

## Correct approach

After checking the applicable document-authority hierarchy, if the conflict remains material:

**Decision:** Should a failed task retry automatically or wait for approval?

**Why it matters:** Document A requires automated retries; document B requires manual recovery. The behavior changes recovery and user oversight.

**Options:**
- **A — Automatic bounded retry:** faster recovery; must control duplicate side effects.
- **B — Manual restart:** stronger human control; slower recovery.
- **C — Hybrid:** automatic retry for explicitly safe, idempotent operations; approval otherwise.

**Recommended:** No selection is safe until the governing requirement and data side effects are established; ask the user to choose or identify the authoritative source.

## Interface behavior

Invoke the actual host's native question tool if exposed: for example Cursor's `AskQuestion`, Claude Code's `AskUserQuestion`, or Codex's currently available user-input interface. Do not output fake tool calls. If unavailable, ask the same concise choice question inline.

Once approved, record the decision ID, evidence, rationale, changed contracts, and affected tasks. Do not infer consent from silence.
