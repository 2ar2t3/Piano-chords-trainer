#!/usr/bin/env python3
"""
main.py
-------
Choix entre l'exercice note unique et l'exercice accord.
"""

from single_note import quiz_loop as note_quiz
from single_chord import chord_quiz

MENU = {
    "1": ("Jouer une NOTE",   note_quiz),
    "2": ("Jouer un ACCORD",  chord_quiz),
}

def main():
    print("\n=== MIDI Trainer ===")
    for k, (label, _) in MENU.items():
        print(f"[{k}] {label}")
    choice = input("Sélection > ").strip()
    MENU.get(choice, ("Option invalide", lambda: None))[1]()

if __name__ == "__main__":
    main()
