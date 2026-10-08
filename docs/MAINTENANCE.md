# Maintainer operations

## Source-of-truth policy

- **Skill behavior:** `skills/prompt-me/SKILL.md` is authoritative.
- **Explanatory docs:** `docs/` are educational companions and must be reconciled if the manifest changes.
- **Examples:** `examples/` are fictional and must remain clearly labelled.
- **Tests:** `scripts/validate.py` and `tests/` validate packaging, not all agent reasoning behavior.
- **Compatibility claims:** keep tied to the observed version or published vendor documentation.

Avoid maintaining several divergent copies of `SKILL.md` inside this repository. The installer copies the same canonical source to each supported agent location.

## Change control

For a behavior change: write the motivating issue → locate conflicting instructions → update canonical manifest → update affected docs/examples → add validation/evaluation evidence → run tests → review cross-agent implications.

Do not silently convert drafting into execution authority or relax approval gates. Never present proposals as locked project decisions.

## Release preparation

1. Verify tests and GitHub Actions are passing for the intended commit.
2. Confirm README/install guide, compatibility, and change history are aligned.
3. Review unresolved issues and security-sensitive changes.
4. Decide a release version, tag and release notes when versioning is actually introduced.
5. Choose a legal distribution license with the owner's explicit decision; do not assume open-source terms.
6. Record known limitations rather than claiming complete compatibility certification.

The repository currently has no published release or fixed support schedule.
