# Operating model

The source of truth for the skill's behavior is [the manifest](../skills/prompt-me/SKILL.md); this document is an explanatory companion.

## Lifecycle

~~~text
User's request and supplied artefacts
           |
           v
  Identify requested output mode
           |
           v
  Read explicit constraints and current state
           |
           v
  Selective, read-only project reconnaissance (if relevant/accessible)
           |
           v
  Evidence and requirements mapping
           |
           +---- Material ambiguity? ----> One concise native decision prompt
           |                                      |
           +<--------- Approved decision ---------+
           |
           v
  Reconstruct faithful target-agent instructions
           |
           +--> Prompt only
           +--> Prompt + execution-ready plan
           +--> Branch-recovery / integration handoff
           +--> Post-merge gap-audit / delivery handoff
           |
           v
  Final self-audit: source coverage, safety, testability, continuity
~~~

## Output modes

| Mode | Trigger | Result |
| --- | --- | --- |
| Prompt refinement | Improve a rough prompt | Self-contained ready-to-paste prompt |
| Project-grounded prompt | Project/repository context is relevant and accessible | Prompt with verified facts and visible unknowns |
| Plan hardening | Existing plan is weak or incomplete | Critical reassessment with atomic tasks when requested |
| Recovery & reconciliation | Interrupted branches or agents | Investigation, decision, and integration gates |
| Build–test–ship handoff | Another agent should execute work | Implementation mandate plus acceptance, verification, and continuation contracts |

A request to **write** a build prompt does not itself authorise the current agent to build or deploy anything.

## Evidence types

The skill differentiates user statements, repository-confirmed facts, directly observed runtime results, inference, proposals, and unknowns. A source being present is not proof it has priority: follow any documented hierarchy in the target repository.

## Read-only first

When a repository is available, inspect the smallest set of sources that can establish the requested outcome, current state, and relevant decisions. Escalate into deeper repository or runtime analysis only when the task calls for it and the environment allows it.

Do not make arbitrary Git changes or access unrelated secrets. When live testing is called for, require an authorised safe environment and distinguish proposed tests from tests actually performed.

## Questions are decision gates

The skill prefers the host's actual question-selection interface if available. It should surface a consequential question **early once enough evidence exists** rather than preparing a long speculative report; it should not repeatedly question routine implementation mechanics.

The question format is covered in [Compatibility](COMPATIBILITY.md), [Quality & safety](QUALITY-AND-SAFETY.md), and [decision example](../examples/04-interactive-decision.md).

## Handoffs

When a plan or agent delegation is requested, the skill provides task input and output contracts with stable identifiers, requirements, source references, decisions, dependencies, acceptance criteria, verification, and exact continuation point. See [A2A protocol](A2A-PROTOCOL.md).

## Limitations

The host agent decides when and how to load the skill, which tools to expose, and whether it can read or run the target project. The skill cannot guarantee model reasoning quality, native UI availability, a complete repository, or a successful deployment.
