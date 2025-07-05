import time, mido

def capture_notes(port, window=0.15) -> set[int]:
    """Renvoie l'ensemble de pitch-classes pressés dans la fenêtre `window`."""
    for msg in port:                                  # première note
        if msg.type == "note_on" and msg.velocity > 0:
            notes = {msg.note % 12}
            t0 = time.time()
            while time.time() - t0 < window:
                for p in port.iter_pending():
                    if p.type == "note_on" and p.velocity > 0:
                        notes.add(p.note % 12)
            return notes
