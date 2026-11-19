#!/usr/bin/env python3
"""Spaced repetition for your glossary (Leitner boxes).

    python scripts/srs.py review   # practice the cards that are due today (max 15)
    python scripts/srs.py stats    # how many cards are in each box

Cards come from work/m01/glossary.md. Progress is saved in srs/state.json (commit it: it is your history).
Box 1 is seen every day. Higher boxes are seen less often: 1, 2, 4, 8, 16 days.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = ROOT / "work" / "m01" / "glossary.md"
STATE = ROOT / "srs" / "state.json"
INTERVALS = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16}
MAX_PER_SESSION = 15


def load_cards() -> Dict[str, Dict[str, str]]:
    if not GLOSSARY.exists():
        sys.exit("No glossary yet. Finish module 01 first (work/m01/glossary.md).")
    cards: Dict[str, Dict[str, str]] = {}
    for block in re.split(r"^## ", GLOSSARY.read_text(encoding="utf-8"), flags=re.M)[1:]:
        term, _, body = block.partition("\n")
        pt = re.search(r"^pt:\s*(.+)$", body, re.M)
        ex = re.search(r"^example:\s*(.+)$", body, re.M)
        if pt and ex:
            cards[term.strip().lower()] = {"pt": pt.group(1), "example": ex.group(1)}
    return cards


def load_state() -> Dict[str, Dict[str, object]]:
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def save_state(state: Dict[str, Dict[str, object]]) -> None:
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2, sort_keys=True))


def review() -> None:
    cards, state, today = load_cards(), load_state(), date.today()
    due: List[str] = [t for t in cards if date.fromisoformat(str(state.get(t, {}).get("due", today.isoformat()))) <= today]
    due = due[:MAX_PER_SESSION]
    if not due:
        print("Nothing to review today. Good job!")
        return
    right = 0
    for term in due:
        input(f"\n  {term.upper()}\n  Say the meaning (in English or Portuguese), then press Enter... ")
        print(f"  pt: {cards[term]['pt']}\n  example: {cards[term]['example']}")
        ok = input("  Did you know it? [y/N] ").strip().lower() == "y"
        box = int(state.get(term, {}).get("box", 1))
        box = min(5, box + 1) if ok else 1
        state[term] = {"box": box, "due": (today + timedelta(days=INTERVALS[box])).isoformat()}
        right += ok
    save_state(state)
    print(f"\nDone: {right}/{len(due)} correct. Progress saved in srs/state.json")


def stats() -> None:
    cards, state = load_cards(), load_state()
    counts = {b: 0 for b in INTERVALS}
    for term in cards:
        counts[int(state.get(term, {}).get("box", 1))] += 1
    for box, n in counts.items():
        print(f"Box {box}: {'#' * n} {n}")
    print(f"Total cards: {len(cards)}")


if __name__ == "__main__":
    {"review": review, "stats": stats}.get(sys.argv[1] if len(sys.argv) > 1 else "", lambda: print(__doc__))()
