"""Seventeen Syllables of Debugging — a haiku about debugging.

Writes one haiku (5-7-5, under 200 characters) to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

HAIKU = (
    "Breakpoint holds its breath.\n"
    "The log swears it saw nothing.\n"
    "I wrote it myself."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
