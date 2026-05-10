---
description: בודק ומעדכן את מתכנן דוקאביב לגרסה האחרונה מ-GitHub
allowed-tools: Bash
---

Run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/update.py"` and surface its output to the user. The script:
- Compares local VERSION to remote VERSION on GitHub
- If a newer remote version exists, downloads all files listed in the manifest and replaces local copies atomically
- Reports what changed (file list + version delta)
- Exits 0 on success, non-zero on network or write errors
