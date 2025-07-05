"""
setup.py
--------
• Contient les tables de correspondance note ↔ pitch-class.
• Ouvre le premier port MIDI disponible et le renvoie.
"""

import sys
import mido

def choose_input_port() -> mido.ports.BaseInput:
    """Return the first available MIDI-IN port or exit."""
    ports = mido.get_input_names()
    if not ports:
        print("No MIDI input port detected.\nPlease plug your keyboard and try again.")
        sys.exit(1)

    # On suppose qu'un seul clavier est branché
    return mido.open_input(ports[0])

def flush_port(port):
    """Vide immédiatement tout le buffer MIDI (note_on, note_off, CC, etc.)."""
    for _ in port.iter_pending():
        pass              # on lit et on jette
