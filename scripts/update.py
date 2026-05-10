#!/usr/bin/env python3
"""Self-update for the docaviv plugin. Stdlib only — no pip installs needed.

Usage:
  python3 update.py           — check and apply updates if a newer version exists
  python3 update.py --check   — check only (silent if already up to date)
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import urllib.request
from pathlib import Path

GITHUB_OWNER = "internet-and-sons"
GITHUB_REPO = "docaviv2026"
GITHUB_BRANCH = "main"
RAW_BASE = (
    f"https://raw.githubusercontent.com/{GITHUB_OWNER}/{GITHUB_REPO}/{GITHUB_BRANCH}"
)

# This file lives at: <plugin_root>/scripts/update.py
# parents[0] = scripts/, [1] = plugin root
PLUGIN_ROOT = Path(__file__).resolve().parents[1]


def fetch(path: str) -> bytes:
    url = f"{RAW_BASE}/{path}"
    req = urllib.request.Request(url, headers={"User-Agent": "docaviv-updater/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read()


def local_version() -> str:
    return (PLUGIN_ROOT / "VERSION").read_text(encoding="utf-8").strip()


def remote_version() -> str:
    return fetch("VERSION").decode("utf-8").strip()


def semver_gt(a: str, b: str) -> bool:
    """Return True if semver string a > b (simple tuple comparison)."""
    def parts(v: str):
        return tuple(int(x) for x in v.lstrip("v").split("."))
    try:
        return parts(a) > parts(b)
    except (ValueError, AttributeError):
        return a > b


def cmd_check() -> int:
    """Exit 0 always; prints one line only if a newer version exists."""
    try:
        remote_v = remote_version()
        local_v = local_version()
        if semver_gt(remote_v, local_v):
            print(f"newer version available: {remote_v} (you have {local_v})")
    except Exception:
        pass  # silent failure — network may be unavailable
    return 0


def cmd_update() -> int:
    try:
        remote_v = remote_version()
    except Exception as e:
        print(f"error: could not reach GitHub — {e}", file=sys.stderr)
        return 1

    local_v = local_version()
    if not semver_gt(remote_v, local_v):
        print(f"already up to date (version {local_v})")
        return 0

    # Fetch manifest from remote
    try:
        manifest = json.loads(fetch(".docaviv-manifest.json").decode("utf-8"))
    except Exception as e:
        print(f"error: could not fetch manifest — {e}", file=sys.stderr)
        return 1

    files = manifest.get("files", [])
    print(f"updating {local_v} → {remote_v} ({len(files)} files)")

    failed = []
    for rel in files:
        target = PLUGIN_ROOT / rel
        try:
            data = fetch(rel)
            target.parent.mkdir(parents=True, exist_ok=True)
            # Atomic write: write to temp file in same dir, then rename
            with tempfile.NamedTemporaryFile(
                delete=False, dir=target.parent, suffix=".tmp"
            ) as tmp:
                tmp.write(data)
                tmp_path = tmp.name
            os.replace(tmp_path, target)
            print(f"  ✓ {rel}")
        except Exception as e:
            # Clean up temp file if it exists
            try:
                os.unlink(tmp_path)
            except Exception:
                pass
            print(f"  ✗ {rel} — {e}", file=sys.stderr)
            failed.append(rel)

    if failed:
        print(f"\nwarning: {len(failed)} file(s) failed to update", file=sys.stderr)
        return 1

    print(f"\ndone. now at version {remote_v}.")
    print("restart Claude Code to pick up the changes.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Self-update the docaviv Claude Code plugin from GitHub."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="check for updates without applying them (silent if up to date)",
    )
    args = parser.parse_args(argv)
    return cmd_check() if args.check else cmd_update()


if __name__ == "__main__":
    sys.exit(main())
