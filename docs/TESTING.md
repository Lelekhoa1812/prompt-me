# Development validation and testing

The project's tests validate the **skill artifact, installer behavior, and documentation linkage**. They do not certify that an LLM will always obey the skill or that every host supports every tool.

## Local checks

Requires Python 3.10+ and Bash. No pip dependencies are needed.

~~~bash
python scripts/validate.py
python -m unittest discover -s tests -p 'test_*.py' -v
bash -n scripts/install.sh tests/test_install.sh
bash tests/test_install.sh
~~~

## Coverage provided

- Portable frontmatter exists with name matching directory and bounded description.
- Main skill instructions include a heading and stay within a reasonable size.
- Repository-local Markdown references resolve.
- Installer dry-run performs no filesystem write at the target path.
- Existing installation is not overwritten without `--force`.
- Replacements retain a backup.
- Cursor, Claude Code, and Codex destination paths are exercised.

## Not provided by these tests

- Cross-agent invocation parity.
- A real agent prompt comparison benchmark.
- Native question-picker availability.
- Verification of private project repositories or production systems.
- Third-party certification or security audit.

For behavior changes, add a **sanitized evaluation scenario** with the starting request, expected decisions/constraints, evidence available, and observed deviations in the target host. Document host version/mode and never claim that a hypothetical scenario was executed.

The GitHub Actions workflow runs repository checks after supported pushes/PRs. A configured workflow is not proof a run succeeded; inspect its actual status.
