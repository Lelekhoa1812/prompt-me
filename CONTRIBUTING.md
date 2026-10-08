# Contributing to prompt-me

Thank you for improving the quality and safety of engineering handoffs.

## Before proposing a change

Read [the problem statement](docs/PROBLEM.md), [operating model](docs/HOW-IT-WORKS.md), and [quality and safety rules](docs/QUALITY-AND-SAFETY.md). Search existing issues to avoid duplicate work.

As of the initial setup, the repository owner has **not selected a license**. Public visibility does not imply permission to redistribute or reuse existing code. If you wish to contribute substantial original material, first discuss licensing and contribution terms with the owner in an issue.

## Development workflow

1. Fork/branch from the latest `main` (after confirming permission/terms).
2. Keep changes focused and identify the underlying failure mode.
3. Do not weaken safeguards merely to shorten instructions.
4. Include a minimal sanitized example for behavior changes.
5. Update documentation and compatibility notes when user-facing behavior changes.
6. Run checks and report actual outcomes:

~~~bash
python scripts/validate.py
python -m unittest discover -s tests -p 'test_*.py' -v
bash -n scripts/install.sh tests/test_install.sh
bash tests/test_install.sh
~~~

7. Open a PR using the template, linking related issues and evidence. PR submission does not guarantee acceptance.

## Technical standards

- Use portable Agent Skills frontmatter; keep `name: prompt-me` matching its directory.
- Make activation text precise: what the skill does and when to use it.
- Keep the instruction core grounded and agent-neutral; put platform-specific caveats in compatibility docs.
- Prefer explicit approval for material architecture/product changes; use native question tools only when actually exposed.
- Never fabricate runtime tests, file paths, commits, or tool availability.
- Preserve the separation of prompt authoring from user-authorised application execution.
- Keep new examples hypothetical and label them; do not imply a real project's private architecture.
- Avoid including credentials, proprietary code, personal data, or sensitive prompt transcripts.

## Reporting security issues

Follow [SECURITY.md](SECURITY.md). Do not publish exploit instructions or secrets in an issue.

## Maintainer decisions

Maintainership, releases, licensing, and acceptance criteria remain controlled by the repository owner until a more formal governance policy is adopted.
