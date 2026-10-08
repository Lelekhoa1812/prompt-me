#!/usr/bin/env python3
"""Validate the portable Agent Skill and repo-local Markdown references.

No third-party dependencies. Does not run or execute SKILL.md instructions.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
ALLOWED = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
REQUIRED = {"name", "description"}


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"Missing skill: {path}"]
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        return [f"{path}: must begin with closed YAML frontmatter"]
    headers: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        h = re.match(r"^([\w-]+):\s*(.*)$", line)
        if not h:
            errors.append(f"{path}: unsupported frontmatter structure: {line[:60]}")
            continue
        key, value = h.groups()
        if key in headers:
            errors.append(f"{path}: duplicate frontmatter field: {key}")
        headers[key] = value
    for field in sorted(REQUIRED - headers.keys()):
        errors.append(f"{path}: missing {field}")
    for field in sorted(headers.keys() - ALLOWED):
        errors.append(f"{path}: unexpected field: {field}")
    name = headers.get("name", "").strip("'\"")
    if not NAME.fullmatch(name) or len(name) > 64 or name != path.parent.name:
        errors.append(f"{path}: name must be a valid kebab-case name matching its directory")
    raw_description = headers.get("description", "")
    if raw_description.startswith('"'):
        try:
            description = json.loads(raw_description)
        except json.JSONDecodeError:
            errors.append(f"{path}: invalid double-quoted description")
            description = ""
    else:
        description = raw_description.strip("'")
    if not isinstance(description, str) or not (1 <= len(description) <= 1024):
        errors.append(f"{path}: description must be 1..1024 characters")
    body = text[match.end():]
    if not re.search(r"(?m)^#\s+\S", body):
        errors.append(f"{path}: missing H1 title")
    if len(text.splitlines()) > 500:
        errors.append(f"{path}: more than 500 lines; split into progressive reference files")
    return errors


def validate_links(root: Path) -> list[str]:
    errors = []
    files = [root / "README.md", root / "CONTRIBUTING.md", root / "SECURITY.md",
             root / "SUPPORT.md", root / "CHANGELOG.md"]
    files += list((root / "docs").rglob("*.md")) if (root / "docs").is_dir() else []
    files += list((root / "examples").rglob("*.md")) if (root / "examples").is_dir() else []
    for source in files:
        if not source.is_file():
            continue
        content = source.read_text(encoding="utf-8")
        for target in LINK.findall(content):
            raw = target.split()[0].strip("<>")
            if raw.startswith(("https://", "http://", "mailto:", "#")):
                continue
            url = urlsplit(raw)
            if url.scheme or not url.path:
                continue
            local = (source.parent / unquote(url.path)).resolve()
            if not local.is_relative_to(root.resolve()):
                errors.append(f"{source.relative_to(root)}: reference escapes repository: {raw}")
            elif not local.exists():
                errors.append(f"{source.relative_to(root)}: broken local link: {raw}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    errors = validate_skill(root / "skills" / "prompt-me" / "SKILL.md")
    errors += validate_links(root)
    for error in errors:
        print(f"FAIL: {error}", file=sys.stderr)
    if errors:
        print(f"Validation failed: {len(errors)} issue(s)", file=sys.stderr)
        return 1
    print("PASS: skill metadata, structure, and local Markdown links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
