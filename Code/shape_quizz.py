#!/usr/bin/env python3
"""
shape_quiz.py
-------------
Quiz « forme d’accord » : l’appli affiche un accord (Cmin, F#maj, Bbmin…)
et l’utilisateur répond par **une seule lettre** :

    W = WHITE        M = MOUNTAIN
    O = OREO         B = BLACK SHEEP
"""

import random
from single_chord import SHAPE_MAP     # table {accord: forme} déjà définie

LETTER_TO_SHAPE = {
    "W": "WHITE",
    "M": "MOUNTAIN",
    "O": "OREO",
    "B": "BLACK SHEEP",
}
VALID_LETTERS = set(LETTER_TO_SHAPE.keys())


def shape_quizz() -> None:
    print("\n▶️  Quiz FORME (W / M / O / B)  –  Ctrl-C pour quitter\n")
    try:
        while True:
            chord = random.choice(list(SHAPE_MAP.keys()))
            correct_shape = SHAPE_MAP[chord]
            correct_letter = next(k for k, v in LETTER_TO_SHAPE.items()
                                  if v == correct_shape)

            # ----- poser la question -----
            answer = input(f"→  {chord}  →  W/M/O/B ? ").strip().upper()

            # ----- valider l’entrée -----
            if answer not in VALID_LETTERS:
                print("    ❓  Tape simplement W, M, O ou B.\n")
                continue

            if answer == correct_letter:
                print("    👍  Correct !\n")
            else:
                print(f"    👎  Faux : réponse attendue {correct_letter} ({correct_shape}).\n")

    except KeyboardInterrupt:
        print("\n👋  Fin du quiz forme.")

shape_quizz()