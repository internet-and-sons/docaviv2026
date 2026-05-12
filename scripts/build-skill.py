#!/usr/bin/env python3
"""Build docaviv2026.skill (a zip of the skill folder) at the repo root.

Run this whenever SKILL.md changes — typically alongside a version bump in
VERSION and .claude-plugin/plugin.json. The output `docaviv2026.skill`
is committed so users without Claude Code can download it directly from
GitHub and upload to Claude.ai via Customize → Skills → Upload skill.

Stdlib only — no pip installs.

Usage:
  python3 scripts/build-skill.py
"""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_SRC = REPO_ROOT / "skills" / "docaviv2026"
OUTPUT = REPO_ROOT / "docaviv2026.skill"


def main() -> int:
    if not (SKILL_SRC / "SKILL.md").exists():
        print(f"error: SKILL.md missing at {SKILL_SRC}", file=sys.stderr)
        return 1
    if not (SKILL_SRC / "data" / "INDEX.md").exists():
        print(
            "error: data/INDEX.md missing. Run scripts/build-skill-data.py first.",
            file=sys.stderr,
        )
        return 1

    if OUTPUT.exists():
        OUTPUT.unlink()

    files_added = 0
    bytes_added = 0
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as z:
        # Walk the entire skill folder; archive every file relative to SKILL_SRC.
        for src in sorted(SKILL_SRC.rglob("*")):
            if not src.is_file():
                continue
            rel = src.relative_to(SKILL_SRC)
            arcname = f"docaviv2026/{rel.as_posix()}"
            z.write(src, arcname=arcname)
            files_added += 1
            bytes_added += src.stat().st_size

    size = OUTPUT.stat().st_size
    print(
        f"wrote {OUTPUT.relative_to(REPO_ROOT)}  "
        f"({size:,} bytes zipped, {files_added} files, {bytes_added:,} raw bytes)",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
