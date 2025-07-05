#!/usr/bin/env python3
"""
single_chord.py
---------------
Exercice : l’appli affiche un accord (ex. Fmin7),
l’utilisateur doit le jouer (n’importe quelle inversion / octave).
"""

import random
import time
import mido

from constantes import CHORDS, PC_TO_NOTE
from setup import choose_input_port
from midi_io import capture_notes  # <— cf. section « Option utilitaire » ci-dessous


def wait_for_chord(port: mido.ports.BaseInput, target_set: set[int],
                   window: float = 0.15) -> bool:
    """
    Agrège toutes les notes jouées dans une fenêtre 'window' (s) après la 1ʳᵉ frappe.
    Retourne True si target_set ⊆ notes_jouées (tolérance aux extensions).
    """
    notes = capture_notes(port, window)          # renvoie un set de pitch-classes
    if notes >= target_set:                      # accepte notes en plus
        print("👍 Correct!")
        return True
    print(f"👎 Faux : tu as joué {sorted(PC_TO_NOTE[n] for n in notes)}")
    return False


def chord_quiz():
    port = choose_input_port()
    print("\n▶️  Exercice ACCORD lancé (Ctrl-C pour quitter).\n")
    try:
        while True:
            name, target = random.choice(list(CHORDS.items()))
            print(f"→  Joue l'accord : {name}")
            wait_for_chord(port, target)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋  Fin de l’exercice accord.")
    finally:
        port.close()
