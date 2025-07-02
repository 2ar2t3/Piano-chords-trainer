"""
single_note.py
--------------
Boucle « devine cette note » : tire une note au hasard,
écoute la réponse (MIDI) et affiche Correct/False.
"""

import random
import time

from setup import *


def wait_for_note(in_port: mido.ports.BaseInput, target_pc: int) -> bool:
    """
    Bloque jusqu'à recevoir un 'note_on' (velocity>0).
    Retourne True si la classe de hauteur (pitch-class) reçue == cible.
    """
    for msg in in_port:
        if msg.type == "note_on" and msg.velocity > 0:
            played_pc   = msg.note % 12
            played_name = PC_TO_NOTE[played_pc]

            if played_pc == target_pc:
                print(f"👍 Correct ! ({played_name})")
                return True
            else:
                print(f"👎 Faux : tu as joué {played_name}, on attendait {PC_TO_NOTE[target_pc]}")
                return False


def quiz_loop():
    """Boucle infinie de quiz."""
    in_port = choose_input_port()
    print("\n▶️  Quiz lancé ! Joue la note demandée (n'importe quelle octave). Ctrl-C pour quitter.\n")

    try:
        while True:
            target_note = random.choice(NOTE_NAMES)
            target_pc   = NOTE_TO_PC[target_note]

            print(f"→  Joue la note : {target_note}")
            wait_for_note(in_port, target_pc)
            time.sleep(1)              # petite pause avant la note suivante
    except KeyboardInterrupt:
        print("\n👋 Fin du quiz. À bientôt !")
    finally:
        in_port.close()
