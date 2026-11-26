#!/usr/bin/env python3
"""Make.fun entry: Funniest One-Line Out-of-Office Reply.

Writes a single out-of-office auto-reply line to /output/entry.txt.
Python 3.13, standard library only.
"""

import os

ENTRY = (
    "Out of office until the 30th. My fern Gary has a watering rota, "
    "a name tag and, as of Tuesday, my parking space."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
