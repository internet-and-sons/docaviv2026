#!/usr/bin/env python3
"""Build docaviv2026.skill (a zip of the skill folder) at the repo root.

Run this whenever SKILL.md, films.json, or plan.py changes — typically
alongside a version bump. The output `docaviv2026.skill` is committed to
the repo so users without Claude Code can download it directly from
GitHub and upload to Claude.ai.

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

# Files to include, relative to SKILL_SRC. Top-level path inside the zip
# is `docaviv2026/...` so the upload is recognized as the "docaviv2026"
# skill — matches what skill-creator's package_skill.py produces.
INCLUDE = [
    "SKILL.md",
    "data/films.json",
    "scripts/plan.py",
]


def main() -> int:
    missing = [rel for rel in INCLUDE if not (SKILL_SRC / rel).exists()]
    if missing:
        print(f"error: missing source files: {missing}", file=sys.stderr)
        return 1

    if OUTPUT.exists():
        OUTPUT.unlink()

    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for rel in INCLUDE:
            src = SKILL_SRC / rel
            arcname = f"docaviv2026/{rel}"
            z.write(src, arcname=arcname)
            print(f"  + {arcname}  ({src.stat().st_size:,} bytes)")

    size = OUTPUT.stat().st_size
    print(f"\nwrote {OUTPUT.relative_to(REPO_ROOT)}  ({size:,} bytes, {len(INCLUDE)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
