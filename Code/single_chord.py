#!/usr/bin/env python3
"""
single_chord.py
---------------
Exercice : l’appli affiche un accord (ex. Fmin7),
l’utilisateur doit le jouer (n’importe quelle inversion / octave).
Affiche aussi la 'shape' mémoire : WHITE, MOUNTAIN, OREO ou BLACK SHEEP.
"""

import random
import time
import mido

from constantes import CHORDS, PC_TO_NOTE
from setup import choose_input_port
from midi_io import capture_notes


# --------------------------------------------------------------------------- #
# 1. TABLE DE CORRESPONDANCE ACCORD → SHAPE  (extrait du PDF « Chords by Shape »)
# --------------------------------------------------------------------------- #
SHAPE_MAP = {
    # WHITE
    "Cmaj": "WHITE",  "Gmaj": "WHITE",  "Fmaj": "WHITE",
    "Amin": "WHITE",  "Emin": "WHITE",  "Dmin": "WHITE",

    # MOUNTAIN
    "Amaj": "MOUNTAIN",  "Emaj": "MOUNTAIN",  "Dmaj": "MOUNTAIN",
    "Cmin": "MOUNTAIN",  "Gmin": "MOUNTAIN",  "Fmin": "MOUNTAIN",

    # OREO  (dièses **et** bémols pour couvrir les deux orthographes)
    "Abmaj": "OREO", "G#maj": "OREO",  "Ebmaj": "OREO", "D#maj": "OREO",
    "Dbmaj": "OREO", "C#maj": "OREO",
    "C#min": "OREO", "Dbmin": "OREO",  "F#min": "OREO", "Gbmin": "OREO",
    "G#min": "OREO", "Abmin": "OREO",

    # BLACK SHEEP
    "Gbmaj": "BLACK SHEEP", "F#maj": "BLACK SHEEP",
    "Bbmaj": "BLACK SHEEP", "A#maj": "BLACK SHEEP",
    "Bmaj":  "BLACK SHEEP",
    "Ebmin": "BLACK SHEEP", "D#min": "BLACK SHEEP",
    "Bbmin": "BLACK SHEEP", "A#min": "BLACK SHEEP",
    "Bmin":  "BLACK SHEEP",
}


def wait_for_chord(port: mido.ports.BaseInput,
                   target_set: set[int],
                   window: float = 0.15) -> None:
    """
    Agrège les notes jouées pendant `window` secondes après la 1ʳᵉ frappe.
    Valide si l'ensemble obtenu == target_set (aucune note en trop).
    """
    while True:
        notes = capture_notes(port, window)
        if notes == target_set:                 # stricte égalité
            print("👍  Correct !\n")
            break
        print(f"👎  Faux : tu as joué "
              f"{', '.join(PC_TO_NOTE[n] for n in sorted(notes))} — réessaie.\n")


def chord_quiz() -> None:
    port = choose_input_port()
    print("\n▶️  Exercice ACCORD lancé (Ctrl-C pour quitter).\n")

    try:
        while True:
            name, target = random.choice(list(CHORDS.items()))
            shape = SHAPE_MAP.get(name)         # None si non répertorié

            # Affichage de la consigne avec ou sans mnémotechnique
            if shape:
                print(f"→  Joue l'accord : {name}   ({shape})")
            else:
                print(f"→  Joue l'accord : {name}")

            wait_for_chord(port, target)
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n👋  Fin de l’exercice accord.")
    finally:
        port.close()
