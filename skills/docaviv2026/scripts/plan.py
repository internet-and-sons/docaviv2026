#!/usr/bin/env python3
"""Docaviv 2026 planning helper — stdlib only, cross-platform.

Subcommands:
  list                       — print all films, one per line (id, name_he, screenings count)
  search <text>              — substring search over name + desc (he/en), case-insensitive
  film <id>                  — print one film with all its screenings, JSON
  day <YYYY-MM-DD>           — list every screening on that date, sorted by time
  single                     — list films with exactly one screening (sorted by date)
  pairs <YYYY-MM-DD> [--gap-min N --gap-max N --hall-strict]
                             — find back-to-back pairs on a given date
                               default gap window: 5–30 minutes
                               --hall-strict requires same hall (otherwise any hall in same venue)
  conflicts <id:datetime> <id:datetime> ...
                             — given a list of "filmId:YYYY-MM-DDTHH:MM" picks,
                               check that none overlap in time. Print OK or list conflicts.
  schedule <id:datetime> ... — print a sorted schedule with travel-time hints

All output is JSON (one object per line for list-style commands), so the agent
can pipe results back into reasoning. Hebrew strings are emitted as-is (UTF-8).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "films.json"


def load() -> dict:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def parse_dt(s: str) -> datetime:
    return datetime.fromisoformat(s)


def fmt_dt(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M")


def emit(obj) -> None:
    print(json.dumps(obj, ensure_ascii=False))


# -------- commands --------

def cmd_list(_args, data) -> int:
    for f in data["films"]:
        emit({
            "id": f.get("id"),
            "name_he": f.get("name_he"),
            "name_en": f.get("name_en"),
            "duration": f.get("duration"),
            "country": f.get("country"),
            "screenings": len(f.get("screenings") or []),
        })
    return 0


def cmd_search(args, data) -> int:
    q = args.text.lower()
    for f in data["films"]:
        hay = " ".join(filter(None, [
            str(f.get("name_he", "")), str(f.get("name_en", "")),
            str(f.get("desc_he", "")), str(f.get("desc_en", "")),
            str(f.get("director", "")), str(f.get("country", "")),
        ])).lower()
        if q in hay:
            emit({
                "id": f.get("id"),
                "name_he": f.get("name_he"),
                "name_en": f.get("name_en"),
                "duration": f.get("duration"),
                "desc_he": f.get("desc_he"),
                "url": f.get("url_en"),
                "screenings": f.get("screenings") or [],
            })
    return 0


def find_film(data, fid):
    for f in data["films"]:
        if str(f.get("id")) == str(fid):
            return f
    return None


def cmd_film(args, data) -> int:
    f = find_film(data, args.id)
    if not f:
        print(json.dumps({"error": "not_found", "id": args.id}, ensure_ascii=False))
        return 1
    emit(f)
    return 0


def cmd_day(args, data) -> int:
    target = args.date  # YYYY-MM-DD
    rows = []
    for f in data["films"]:
        for s in f.get("screenings") or []:
            dt = s.get("datetime", "")
            if dt.startswith(target):
                start = parse_dt(dt)
                dur = f.get("duration") or 0
                end = start + timedelta(minutes=int(dur)) if dur else None
                rows.append({
                    "id": f.get("id"),
                    "name_he": f.get("name_he"),
                    "name_en": f.get("name_en"),
                    "start": fmt_dt(start),
                    "end": fmt_dt(end) if end else None,
                    "duration": dur,
                    "venue_he": s.get("venue_he"),
                    "hall": s.get("hall"),
                    "order": s.get("order"),
                    "url": f.get("url_en"),
                })
    rows.sort(key=lambda r: r["start"])
    for r in rows:
        emit(r)
    return 0


def cmd_single(_args, data) -> int:
    rows = []
    for f in data["films"]:
        scr = f.get("screenings") or []
        if len(scr) == 1:
            s = scr[0]
            rows.append({
                "id": f.get("id"),
                "name_he": f.get("name_he"),
                "name_en": f.get("name_en"),
                "duration": f.get("duration"),
                "datetime": s.get("datetime"),
                "venue_he": s.get("venue_he"),
                "order": s.get("order"),
                "url": f.get("url_en"),
                "desc_he": f.get("desc_he"),
            })
    rows.sort(key=lambda r: r.get("datetime") or "")
    for r in rows:
        emit(r)
    return 0


def cmd_pairs(args, data) -> int:
    target = args.date
    gmin = args.gap_min
    gmax = args.gap_max
    strict = args.hall_strict

    # Collect screenings on that date with computed end times (need duration)
    screenings = []
    for f in data["films"]:
        dur = f.get("duration")
        for s in f.get("screenings") or []:
            dt = s.get("datetime", "")
            if not dt.startswith(target):
                continue
            if not dur:
                continue
            start = parse_dt(dt)
            end = start + timedelta(minutes=int(dur))
            screenings.append({
                "film": f, "show": s, "start": start, "end": end,
            })

    pairs = []
    for a in screenings:
        for b in screenings:
            if a["film"].get("id") == b["film"].get("id"):
                continue
            gap = (b["start"] - a["end"]).total_seconds() / 60.0
            if not (gmin <= gap <= gmax):
                continue
            if strict and a["show"].get("hall") != b["show"].get("hall"):
                continue
            pairs.append({
                "gap_min": int(gap),
                "first": {
                    "id": a["film"].get("id"),
                    "name_he": a["film"].get("name_he"),
                    "start": fmt_dt(a["start"]),
                    "end": fmt_dt(a["end"]),
                    "venue_he": a["show"].get("venue_he"),
                    "hall": a["show"].get("hall"),
                    "order": a["show"].get("order"),
                    "url": a["film"].get("url_en"),
                },
                "second": {
                    "id": b["film"].get("id"),
                    "name_he": b["film"].get("name_he"),
                    "start": fmt_dt(b["start"]),
                    "end": fmt_dt(b["end"]),
                    "venue_he": b["show"].get("venue_he"),
                    "hall": b["show"].get("hall"),
                    "order": b["show"].get("order"),
                    "url": b["film"].get("url_en"),
                },
            })
    pairs.sort(key=lambda p: p["first"]["start"])
    for p in pairs:
        emit(p)
    return 0


def parse_pick(token: str):
    if ":" not in token:
        raise ValueError(f"bad pick (need id:datetime): {token}")
    fid, _, dt = token.partition(":")
    return fid, dt


def resolve_picks(data, tokens):
    out = []
    for t in tokens:
        fid, dt = parse_pick(t)
        f = find_film(data, fid)
        if not f:
            return None, f"film not found: {fid}"
        # Find matching screening
        s = next((x for x in (f.get("screenings") or []) if x.get("datetime") == dt), None)
        if not s:
            return None, f"screening not found for film {fid} at {dt}"
        dur = f.get("duration") or 0
        start = parse_dt(dt)
        end = start + timedelta(minutes=int(dur)) if dur else start + timedelta(minutes=90)
        out.append({"film": f, "show": s, "start": start, "end": end})
    return out, None


def cmd_conflicts(args, data) -> int:
    picks, err = resolve_picks(data, args.picks)
    if err:
        emit({"ok": False, "error": err})
        return 1
    picks_sorted = sorted(picks, key=lambda p: p["start"])
    conflicts = []
    for i in range(len(picks_sorted) - 1):
        a = picks_sorted[i]
        b = picks_sorted[i + 1]
        if b["start"] < a["end"]:
            conflicts.append({
                "a": {"id": a["film"].get("id"), "name_he": a["film"].get("name_he"),
                      "start": fmt_dt(a["start"]), "end": fmt_dt(a["end"])},
                "b": {"id": b["film"].get("id"), "name_he": b["film"].get("name_he"),
                      "start": fmt_dt(b["start"]), "end": fmt_dt(b["end"])},
                "overlap_min": int((a["end"] - b["start"]).total_seconds() / 60),
            })
    if conflicts:
        emit({"ok": False, "conflicts": conflicts})
        return 2
    emit({"ok": True, "count": len(picks_sorted)})
    return 0


def cmd_schedule(args, data) -> int:
    picks, err = resolve_picks(data, args.picks)
    if err:
        emit({"ok": False, "error": err})
        return 1
    picks_sorted = sorted(picks, key=lambda p: p["start"])
    items = []
    for i, p in enumerate(picks_sorted):
        item = {
            "order_index": i + 1,
            "id": p["film"].get("id"),
            "name_he": p["film"].get("name_he"),
            "name_en": p["film"].get("name_en"),
            "start": fmt_dt(p["start"]),
            "end": fmt_dt(p["end"]),
            "duration": p["film"].get("duration"),
            "venue_he": p["show"].get("venue_he"),
            "hall": p["show"].get("hall"),
            "order": p["show"].get("order"),
            "url": p["film"].get("url_en"),
        }
        if i > 0:
            prev = picks_sorted[i - 1]
            gap = int((p["start"] - prev["end"]).total_seconds() / 60)
            item["gap_from_prev_min"] = gap
            item["overlap"] = gap < 0
            item["same_hall"] = prev["show"].get("hall") == p["show"].get("hall")
        items.append(item)
    emit({"ok": all(not it.get("overlap") for it in items[1:]), "schedule": items})
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="plan.py")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list")

    sp = sub.add_parser("search")
    sp.add_argument("text")

    sp = sub.add_parser("film")
    sp.add_argument("id")

    sp = sub.add_parser("day")
    sp.add_argument("date", help="YYYY-MM-DD")

    sub.add_parser("single")

    sp = sub.add_parser("pairs")
    sp.add_argument("date", help="YYYY-MM-DD")
    sp.add_argument("--gap-min", type=int, default=5)
    sp.add_argument("--gap-max", type=int, default=30)
    sp.add_argument("--hall-strict", action="store_true")

    sp = sub.add_parser("conflicts")
    sp.add_argument("picks", nargs="+", help="id:YYYY-MM-DDTHH:MM ...")

    sp = sub.add_parser("schedule")
    sp.add_argument("picks", nargs="+", help="id:YYYY-MM-DDTHH:MM ...")

    args = p.parse_args(argv)
    data = load()
    return {
        "list": cmd_list,
        "search": cmd_search,
        "film": cmd_film,
        "day": cmd_day,
        "single": cmd_single,
        "pairs": cmd_pairs,
        "conflicts": cmd_conflicts,
        "schedule": cmd_schedule,
    }[args.cmd](args, data)


if __name__ == "__main__":
    sys.exit(main())
