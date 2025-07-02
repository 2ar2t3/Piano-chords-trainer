"""
setup.py
--------
• Contient les tables de correspondance note ↔ pitch-class.
• Ouvre le premier port MIDI disponible et le renvoie.
"""

import sys
import mido

# Notes names in MIDI numerical order
NOTE_NAMES = ["C", "C#", "D", "D#", "E",
              "F", "F#", "G", "G#", "A", "A#", "B"]

# Dictionnaires de conversion
NOTE_TO_PC = {name: pc for pc, name in enumerate(NOTE_NAMES)}
PC_TO_NOTE = {pc: name for name, pc in NOTE_TO_PC.items()}


def choose_input_port() -> mido.ports.BaseInput:
    """Return the first available MIDI-IN port or exit."""
    ports = mido.get_input_names()
    if not ports:
        print("No MIDI input port detected.\nPlease plug your keyboard and try again.")
        sys.exit(1)

    # On suppose qu'un seul clavier est branché
    return mido.open_input(ports[0])
