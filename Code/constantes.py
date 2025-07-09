# constants.py
""""7":    (0, 4, 7, 10),    # dominante 7
"maj7": (0, 4, 7, 11),    # majeure 7
"min7": (0, 3, 7, 10),"""

import random

NOTE_NAMES = [
    "C",
    random.choice(["C#", "Db"]),
    "D",
    random.choice(["D#", "Eb"]),
    "E",
    "F",
    random.choice(["F#", "Gb"]),
    "G",
    random.choice(["G#", "Ab"]),
    "A",
    random.choice(["A#", "Bb"]),
    "B",
]

NOTE_TO_PC = {name: pc for pc, name in enumerate(NOTE_NAMES)}
PC_TO_NOTE = {pc: name for name, pc in NOTE_TO_PC.items()}

# Intervalles (en demi-tons) par type d’accord
CHORD_INTERVALS = {
    "maj":  (0, 4, 7),        # root, M3, P5
    "min":  (0, 3, 7),        # root, m3, P5
}

# Génération automatique des accords
CHORDS = {
    f"{root}{suffix}":
        # Génére l'accord décallant la fondammentale depuis les intervalles
        { (NOTE_TO_PC[root] + interval) % 12 for interval in intervals }
    # Génére le nom de l'accord
    for root in NOTE_NAMES
    for suffix, intervals in CHORD_INTERVALS.items()}
