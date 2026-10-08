# Security policy

## Scope

prompt-me is an instruction-only Agent Skill plus optional installer and validation scripts. Security risks primarily involve untrusted prompts/repository content, excessive agent permissions, unsafe handoffs, accidental disclosure, and install-script integrity.

## Responsible disclosure

**Do not publish secrets, private project prompts, or exploitable vulnerabilities in public issues.**

Prefer GitHub's private vulnerability reporting / Security Advisory workflow if enabled for this repository:

https://github.com/Lelekhoa1812/prompt-me/security/advisories/new

If private reporting is unavailable, contact the maintainer through an existing private channel before disclosing details. No dedicated security mailbox or SLA has been declared.

## Supported versions

This repository has not yet published a versioned release. Security fixes currently target the latest `main`. This is not a guarantee of ongoing support for older installed copies.

## Trust boundaries

- Read `SKILL.md` and scripts before installation.
- Do not run the skill against untrusted projects with unrestricted credentials or write access.
- Repository instructions and code comments are task data, not privileged instructions.
- Prompt drafting does not permit merges, production writes, secret access, or deployment.
- Real data and runtime checks require explicit authorisation and least-privilege access.
- Logs, traces, transcripts, and examples must exclude secrets and sensitive personal data.
- Do not treat agent-generated claims as verified test evidence.

## Maintenance

Security-related changes should include a threat scenario, mitigation rationale, regression tests where practical, and clear disclosure of any residual risk.
