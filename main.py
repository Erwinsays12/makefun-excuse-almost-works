#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun entry.

Writes one line of plain text to /output/entry.txt: the single line a
gamer texts the boss to skip work on GTA 6 launch week.

The line is fixed and deterministic: the grader runs the program twice
and both runs must produce the same text. It is chosen to read like a
real text sent in a hurry — one line, plain words, no setup, no
explanation, no signature — and to give a tired manager a specific,
boring, believable detail (council roadworks boxing a car in) instead
of one of the obvious excuses (a dead grandmother, a flat tyre, a
sudden fever). The humour comes from the excuse's own logic: the car
is fine, the street simply is not passable.
"""

import sys
from pathlib import Path

EXCUSE = (
    "Sorry, the council dug up my street overnight and my car's "
    "boxed in behind the barriers"
)

MAX_WORDS = 20
MAX_CHARS = 140


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    output_path = Path(argv[0]) if argv else Path("/output/entry.txt")

    words = EXCUSE.split()
    assert 1 <= len(EXCUSE) <= MAX_CHARS, "excuse must be 1-140 characters"
    assert len(words) <= MAX_WORDS, "excuse must be at most 20 words"
    assert "\n" not in EXCUSE, "excuse must be a single line"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(EXCUSE, encoding="utf-8")

    # Read it back: the grader scores exactly what is on disk, so fail
    # loudly here rather than shipping a truncated or altered file.
    written = output_path.read_text(encoding="utf-8")
    assert written == EXCUSE, "read-back differs from the intended excuse"

    print(f"wrote {len(EXCUSE)} chars, {len(words)} words to {output_path}")


if __name__ == "__main__":
    main()
