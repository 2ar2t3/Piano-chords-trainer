#!/usr/bin/env python3
"""
shape_quiz.py
-------------
Quiz « forme d’accord » configurable :
modifie SELECTED_SHAPES pour filtrer les catégories.
"""

import random
from single_chord import SHAPE_MAP     # {accord : forme}

# ──────────────────────────────────────────────────────────────────────────────
# Modifie ici pour choisir tes formes (ex. {"WHITE", "MOUNTAIN", "OREO"})
SELECTED_SHAPES = {"WHITE", "MOUNTAIN", "OREO"}
# ──────────────────────────────────────────────────────────────────────────────

FILTERED_CHORDS = {acc: shp for acc, shp in SHAPE_MAP.items()
                   if shp in SELECTED_SHAPES}

LETTER_TO_SHAPE = {
    "W": "WHITE",
    "M": "MOUNTAIN",
    "O": "OREO",
    "B": "BLACK SHEEP",
}

VALID_LETTERS = {k for k, v in LETTER_TO_SHAPE.items() if v in SELECTED_SHAPES}


def shape_quiz() -> None:
    if not FILTERED_CHORDS:
        print("⚠️  Aucun accord ne correspond aux formes choisies dans "
              "SELECTED_SHAPES.")
        return

    label = " / ".join(sorted(VALID_LETTERS))
    print(f"\n▶️  Quiz FORME ({label}) – Ctrl-C pour quitter\n")

    try:
        while True:
            chord, shape = random.choice(list(FILTERED_CHORDS.items()))
            correct_letter = next(k for k, v in LETTER_TO_SHAPE.items()
                                  if v == shape)

            answer = input(f"→  {chord}  →  {label} ? ").strip().upper()

            if answer not in VALID_LETTERS:
                print(f"    ❓  Tape {label} uniquement.\n")
                continue

            if answer == correct_letter:
                print("    👍  Correct !\n")
            else:
                print(f"    👎  Faux : c’était {correct_letter} ({shape}).\n")

    except KeyboardInterrupt:
        print("\n👋  Fin du quiz forme.")

shape_quiz()
