#!/usr/bin/env python3
"""
Build a ready-to-import Anki deck (.apkg) from secai-plus-flashcards.tsv.

The TSV (Front<TAB>Back<TAB>Tags) already imports directly into Anki, so this
script is OPTIONAL — use it only if you want a single double-click .apkg file.

Usage:
    pip install genanki
    python build_apkg.py
    # -> produces secai-plus.apkg  (File > Import in Anki, or double-click)

Unofficial / community study material. Verify against the official CompTIA
SecAI+ objectives. See ../exam-objectives.md.
"""
import csv
import os
import sys

try:
    import genanki
except ImportError:
    sys.exit("genanki not installed. Run:  pip install genanki")

HERE = os.path.dirname(os.path.abspath(__file__))
TSV = os.path.join(HERE, "secai-plus-flashcards.tsv")
OUT = os.path.join(HERE, "secai-plus.apkg")

# Stable, arbitrary IDs (keep constant so re-imports update rather than duplicate).
MODEL_ID = 1607392319
DECK_ID = 2059400110

model = genanki.Model(
    MODEL_ID,
    "SecAI+ Basic",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{
        "name": "Card 1",
        "qfmt": "{{Front}}",
        "afmt": '{{FrontSide}}<hr id="answer">{{Back}}',
    }],
    css=".card{font-family:arial;font-size:18px;text-align:left;color:#111;"
        "background:#fff;padding:16px;} hr#answer{margin:14px 0;}",
)

deck = genanki.Deck(DECK_ID, "CompTIA SecAI+ (Unofficial)")

count = 0
with open(TSV, encoding="utf-8") as f:
    for row in csv.reader(f, delimiter="\t"):
        if not row or len(row) < 2:
            continue
        front, back = row[0], row[1]
        tags = row[2].split() if len(row) > 2 and row[2] else []
        deck.add_note(genanki.Note(model=model, fields=[front, back], tags=tags))
        count += 1

genanki.Package(deck).write_to_file(OUT)
print(f"Wrote {OUT} with {count} cards.")
