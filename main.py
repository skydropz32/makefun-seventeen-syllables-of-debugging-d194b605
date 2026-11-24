"""Seventeen Syllables of Debugging — a haiku about debugging.

Writes one haiku to /output/entry.txt. Syllable structure 5-7-5
(17 syllables total):

    Breakpoint holds its breath.      (5: Break-point-holds-its-breath)
    The log swears it saw nothing.   (7: The-log-swears-it-saw-noth-ing)
    I wrote it myself.               (5: I-wrote-it-my-self)

The competition gate requires 1-200 UTF-8 characters, not
whitespace-only; the program fails loudly instead of writing an
entry that can never score. Deterministic: the same bytes on
every run.
"""

import os

HAIKU = (
    "Breakpoint holds its breath.\n"
    "The log swears it saw nothing.\n"
    "I wrote it myself."
)


def main() -> None:
    # Fail loudly if the haiku ever leaves the 1-200 character gate.
    if not 1 <= len(HAIKU) <= 200 or not HAIKU.strip():
        raise SystemExit(
            f"haiku is {len(HAIKU)} characters, must be 1-200 non-blank"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
