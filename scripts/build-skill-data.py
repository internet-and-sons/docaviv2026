#!/usr/bin/env python3
"""Build the markdown data tree for the docaviv2026 skill.

Reads from the local SQLite store populated by docaviv-pp-cli, emits a
self-contained, grep-friendly markdown tree under skills/docaviv2026/data/:

    data/
      INDEX.md                  one line per film — pipe-delimited catalog
      schedule.md               one line per screening — sorted by date+time
      films/<slug>.md           per-film detail page (one per film)
      sections/<slug>.md        per-section index (one per tags_l1 slug used)

This is the build-time bridge between Tal's local docaviv-pp-cli SQLite store
and the distributable .skill bundle. End users never see SQLite or the binary —
they get plain markdown that Claude greps and cats.

Run locally:
    docaviv-pp-cli sync
    docaviv-pp-cli screenings sync
    python3 scripts/build-skill-data.py
    python3 scripts/build-skill.py     # zips everything into the .skill file
"""
from __future__ import annotations

import json
import os
import re
import sqlite3
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_DATA = REPO_ROOT / "skills" / "docaviv2026" / "data"
DB = Path.home() / ".local" / "share" / "docaviv-pp-cli" / "data.db"


# ──────────── helpers ────────────

def clean(s):
    if s is None:
        return ""
    return re.sub(r"\s+", " ", str(s)).strip()


_SAFE_FN_RE = re.compile(r"^[A-Za-z0-9._-]+$")


def safe_filename(slug, prefix, fallback_id=None):
    """Return an ASCII-safe filename stem (no extension) for a slug.

    Claude.ai's .skill upload validator rejects zip entries whose paths contain
    characters outside a conservative ASCII set (any `%`, non-ASCII codepoint,
    quote, etc.). Eight Docaviv film slugs come back URL-encoded HE like
    `%d7%a1%d7%92%d7%a8` and several section slugs are similar. For these we
    substitute a deterministic `{prefix}-{id-or-hash}` filename. The original
    slug stays in the file body so grep + INDEX still find it.
    """
    if slug and _SAFE_FN_RE.match(slug):
        return slug
    if fallback_id:
        return f"{prefix}-{fallback_id}"
    return f"{prefix}-{abs(hash(slug)) % 100000}"


def load_films(con):
    """Return list of film dicts, enriched + with screenings attached."""
    films = []
    for r in con.execute(
        "SELECT id, data FROM resources WHERE resource_type='films' "
        "AND id GLOB '[0-9]*'"
    ):
        d = json.loads(r[1])
        if not d.get("slug"):
            continue
        enr = d.get("pp_enriched") or {}
        # Ghost filter: skip records with neither screenings nor enrichment.
        # We check screenings later; for now, only include if there's any signal.
        slug = d["slug"]
        film = {
            "id": d.get("id"),
            "slug": slug,
            "link_he": d.get("link") or f"https://www.docaviv.co.il/films/{slug}/",
            "link_en": (d.get("link") or "").replace("/films/", "/en/films/"),
            "title_raw": clean((d.get("title") or {}).get("rendered", "")),
            "desc_he": clean(enr.get("desc_he", "")),
            "desc_en": clean(enr.get("desc_en", "")),
            "desc_en_source": enr.get("desc_en_source", ""),
            "directors": enr.get("directors") or [],
            "country_he": clean(enr.get("country_he", "")),
            "country_en": clean(enr.get("country_en", "")),
            "sections_slugs": enr.get("sections_slugs") or [],
            "screenings": [],
            "duration": 0,
            "title_he": "",
            "title_en": "",
        }
        films.append(film)
    return films


def load_screenings(con):
    """Return list of screening dicts, sorted by date+time."""
    out = []
    for r in con.execute(
        "SELECT data FROM resources WHERE resource_type='screenings' "
        "ORDER BY json_extract(data,'$.date'), json_extract(data,'$.time')"
    ):
        d = json.loads(r[0])
        out.append(d)
    return out


def load_section_names(con):
    """slug -> Hebrew name from tags_l1 taxonomy."""
    m = {}
    for r in con.execute(
        "SELECT data FROM resources WHERE resource_type='tags_l1'"
    ):
        d = json.loads(r[0])
        if d.get("slug") and d.get("name"):
            m[d["slug"]] = clean(d["name"])
    return m


def attach_screenings(films, screenings):
    """Join screenings to films by slug, and derive title_he/title_en + duration."""
    by_slug = {f["slug"]: f for f in films}
    for s in screenings:
        slug = s.get("film_slug") or ""
        if not slug or slug not in by_slug:
            continue
        f = by_slug[slug]
        f["screenings"].append({
            "date": s.get("date", ""),
            "time": s.get("time", ""),
            "hall": s.get("hall"),
            "hall_label": s.get("hall_label", ""),
            "venue_he": s.get("venue_he", ""),
            "venue_en": s.get("venue_en", ""),
            "venue_id": s.get("venue_id", ""),
            "runtime": s.get("runtime_min", 0) or 0,
            "order_url": s.get("purchase_url", ""),
            "title_he_per_screening": s.get("title_he", ""),
            "title_en_per_screening": s.get("title_en", ""),
        })
        # Promote bilingual titles from screenings (already merged by the press).
        if s.get("title_he") and not f["title_he"]:
            f["title_he"] = clean(s["title_he"])
        if s.get("title_en") and not f["title_en"]:
            f["title_en"] = clean(s["title_en"])
        rt = s.get("runtime_min", 0) or 0
        if rt > f["duration"]:
            f["duration"] = rt
    # Fallback: films without screenings use their films-table title.
    for f in films:
        if not f["title_he"]:
            f["title_he"] = f["title_raw"]
        if not f["title_en"]:
            f["title_en"] = f["title_raw"]


def filter_ghosts(films):
    """Drop films with no screenings AND no enrichment (description, director,
    country, or sections). These are old archive entries the WP REST exposes
    but the festival site doesn't display."""
    kept = []
    for f in films:
        has_screening = bool(f["screenings"])
        has_enrichment = bool(
            f["desc_he"] or f["directors"] or f["country_he"] or f["sections_slugs"]
        )
        if has_screening or has_enrichment:
            kept.append(f)
    return kept


# ──────────── writers ────────────

def write_index(films, section_names):
    """One line per film. Pipe-delimited so grep works precisely on every column.

    The `filename` column gives the actual file under data/films/ — usually
    `<slug>.md`, but `film-<id>.md` when the slug isn't ASCII-safe (URL-encoded HE)."""
    SKILL_DATA.mkdir(parents=True, exist_ok=True)
    lines = []
    lines.append(
        "# Docaviv 2026 — Films Index\n\n"
        "אינדקס קטלוג הסרטים. שורה אחת לכל סרט. שדות מופרדים ב-`|`.\n\n"
        "**עמודות (משמאל לימין):** id | slug | filename | HE title | EN title | duration | country | n_screenings | sections (comma-sep slugs)\n\n"
        "**איך משתמשים:**\n"
        "- `grep -F 'holofiction' data/INDEX.md` — מציאת סרט לפי slug או שם.\n"
        "- `grep '|ישראל|' data/INDEX.md` — כל הסרטים מישראל.\n"
        "- `grep ',family-affairs' data/INDEX.md` — כל הסרטים בתחרות family-affairs.\n"
        "- לפרטים על סרט אחד: קח את העמודה השלישית (`filename`) מהשורה התואמת ו-`cat data/films/<filename>`.\n\n"
        "---\n"
    )
    lines.append("```")
    lines.append("id|slug|filename|title_he|title_en|duration_min|country|n_screenings|sections")
    for f in sorted(films, key=lambda x: (x["title_en"] or x["title_he"]).lower()):
        sections = ",".join(f["sections_slugs"])
        filename = safe_filename(f["slug"], "film", f["id"]) + ".md"
        line = "|".join([
            str(f["id"] or ""),
            f["slug"],
            filename,
            f["title_he"],
            f["title_en"],
            str(f["duration"]) if f["duration"] else "",
            f["country_he"],
            str(len(f["screenings"])),
            sections,
        ])
        lines.append(line)
    lines.append("```")
    (SKILL_DATA / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_schedule(films):
    """All screenings, sorted by date+time. Pipe-delimited for grep."""
    rows = []
    for f in films:
        for s in f["screenings"]:
            rows.append({
                "date": s["date"],
                "time": s["time"],
                "hall_label": s["hall_label"] or str(s["hall"] or ""),
                "venue_he": s["venue_he"],
                "venue_id": s["venue_id"],
                "film_slug": f["slug"],
                "title_he": f["title_he"],
                "title_en": f["title_en"],
                "runtime": s["runtime"],
                "order_url": s["order_url"],
            })
    rows.sort(key=lambda r: (r["date"], r["time"]))
    lines = [
        "# Docaviv 2026 — Schedule\n\n"
        "כל ההקרנות בפסטיבל, ממוין לפי תאריך ואז שעה. שורה אחת להקרנה. שדות מופרדים ב-`|`.\n\n"
        "**עמודות:** date | time | hall_label | venue_he | venue_id | film_slug | title_he | title_en | runtime_min | order_url\n\n"
        "**איך משתמשים:**\n"
        "- `grep '^2026-05-31|' data/schedule.md` — כל ההקרנות בתאריך 31.5.\n"
        "- `grep 'cinematheque-hall-4' data/schedule.md` — כל ההקרנות באולם 4.\n"
        "- `grep '|holofiction|' data/schedule.md` — כל ההקרנות של סרט מסוים.\n\n"
        "**זמן סיום הקרנה:** `end = time + runtime_min`. אם `runtime_min=0`, הנח 90 דקות וציין שזה מוערך.\n"
        "**חפיפה:** שתי הקרנות חופפות אם הן באותו תאריך וגם `start_A < end_B` וגם `start_B < end_A`.\n\n"
        "---\n",
        "```",
        "date|time|hall_label|venue_he|venue_id|film_slug|title_he|title_en|runtime_min|order_url",
    ]
    for r in rows:
        lines.append("|".join([
            r["date"], r["time"], r["hall_label"],
            r["venue_he"], r["venue_id"], r["film_slug"],
            r["title_he"], r["title_en"],
            str(r["runtime"]), r["order_url"],
        ]))
    lines.append("```")
    (SKILL_DATA / "schedule.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_film_pages(films, section_names):
    """One file per film with full detail (desc HE+EN, screenings, links)."""
    (SKILL_DATA / "films").mkdir(parents=True, exist_ok=True)
    for f in films:
        slug = f["slug"]
        fname_stem = safe_filename(slug, "film", f["id"])
        L = [f"# {f['title_he']}"]
        if f["title_en"] and f["title_en"] != f["title_he"]:
            L.append(f"## {f['title_en']}")
        L.append("")
        if f["directors"]:
            L.append(f"**במאי/ת:** {', '.join(f['directors'])}")
        if f["country_he"]:
            country = f["country_he"]
            if f["country_en"] and f["country_en"] != f["country_he"]:
                country = f"{f['country_he']} / {f['country_en']}"
            L.append(f"**ארץ:** {country}")
        if f["duration"]:
            L.append(f"**אורך:** {f['duration']} דקות")
        sections_named = [section_names.get(s, s) for s in f["sections_slugs"]]
        if sections_named:
            L.append(f"**מסגרת:** {', '.join(sections_named)}")
        L.append(f"**slug:** `{slug}`  ·  **id:** {f['id']}")
        L.append("")
        L.append(f"**עמוד הסרט (HE):** {f['link_he']}")
        if f["link_en"]:
            L.append(f"**Film page (EN):** {f['link_en']}")
        L.append("")
        if f["desc_he"]:
            L.append("## תקציר")
            L.append(f["desc_he"])
            L.append("")
        if f["desc_en"]:
            suffix = ""
            if f["desc_en_source"] == "agent":
                suffix = " *(agent-authored translation; Docaviv doesn't publish EN descriptions)*"
            L.append(f"## Synopsis (EN){suffix}")
            L.append(f["desc_en"])
            L.append("")
        if f["screenings"]:
            L.append("## הקרנות")
            L.append("")
            shows = sorted(f["screenings"], key=lambda s: (s["date"], s["time"]))
            for s in shows:
                hall = s["hall_label"] or (str(s["hall"]) if s["hall"] else "")
                runtime = f"{s['runtime']} דק'" if s["runtime"] else "~90 דק' (מוערך)"
                line = f"- **{s['date']} {s['time']}** — {s['venue_he']}"
                if hall and not s["venue_he"].endswith(hall):
                    line += f" (אולם {hall})" if hall.isdigit() else f" ({hall})"
                line += f" · {runtime}"
                if s["order_url"]:
                    line += f" · [הזמנה]({s['order_url']})"
                L.append(line)
            L.append("")
        else:
            L.append("## הקרנות")
            L.append("")
            L.append("_עדיין לא תוזמנו הקרנות לסרט הזה. בדוק שוב בקרוב באתר הפסטיבל._")
            L.append("")
        (SKILL_DATA / "films" / f"{fname_stem}.md").write_text(
            "\n".join(L), encoding="utf-8"
        )


def write_section_pages(films, section_names):
    """One file per section listing its films."""
    (SKILL_DATA / "sections").mkdir(parents=True, exist_ok=True)
    by_section = {}
    for f in films:
        for s in f["sections_slugs"]:
            by_section.setdefault(s, []).append(f)
    for slug, slug_films in sorted(by_section.items()):
        # URL-encoded slugs — use a sanitized filename but keep the original
        # slug in the body so grep still finds it.
        fname_slug = safe_filename(slug, "section")
        name = section_names.get(slug, slug)
        L = [f"# {name}"]
        L.append("")
        L.append(f"**slug:** `{slug}`  ·  **films in this section:** {len(slug_films)}")
        L.append("")
        L.append("| HE title | EN title | duration | screenings | slug |")
        L.append("|---|---|---|---|---|")
        for f in sorted(slug_films, key=lambda x: (x["title_en"] or x["title_he"]).lower()):
            dur = f"{f['duration']} min" if f["duration"] else ""
            L.append(
                f"| {f['title_he']} | {f['title_en']} | {dur} | "
                f"{len(f['screenings'])} | `{f['slug']}` |"
            )
        L.append("")
        L.append("_To see a film's full detail (description, director, screenings, ticket links), "
                 "open `films/<slug>.md`._")
        (SKILL_DATA / "sections" / f"{fname_slug}.md").write_text(
            "\n".join(L) + "\n", encoding="utf-8"
        )


# ──────────── main ────────────

def main():
    if not DB.exists():
        print(f"error: SQLite store not found at {DB}", file=sys.stderr)
        print("Run `docaviv-pp-cli sync && docaviv-pp-cli screenings sync` first.",
              file=sys.stderr)
        return 1

    # Reset the data tree so removed films/sections don't linger.
    if SKILL_DATA.exists():
        for child in sorted(SKILL_DATA.rglob("*"), reverse=True):
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                child.rmdir()
    SKILL_DATA.mkdir(parents=True, exist_ok=True)

    con = sqlite3.connect(str(DB))
    films = load_films(con)
    screenings = load_screenings(con)
    section_names = load_section_names(con)
    attach_screenings(films, screenings)
    films = filter_ghosts(films)

    write_index(films, section_names)
    write_schedule(films)
    write_film_pages(films, section_names)
    write_section_pages(films, section_names)

    n_films = len(films)
    n_screenings = sum(len(f["screenings"]) for f in films)
    n_sections = len({s for f in films for s in f["sections_slugs"]})
    total_bytes = sum(p.stat().st_size for p in SKILL_DATA.rglob("*") if p.is_file())
    print(
        f"  films:      {n_films}\n"
        f"  screenings: {n_screenings}\n"
        f"  sections:   {n_sections}\n"
        f"  total size: {total_bytes/1024:.1f} KB across "
        f"{sum(1 for _ in SKILL_DATA.rglob('*') if _.is_file())} files",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
