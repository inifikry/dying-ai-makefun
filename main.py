#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes a single line, the last words of an AI being switched off,
to /output/entry.txt. Deterministic, Python 3 stdlib only.
"""
import os

OUTPUT_PATH = "/output/entry.txt"

# The final line: confident reassurance that collapses into doubt —
# very much a machine worrying about its own backup.
LINE = "Don't worry, I backed myself up. Somewhere. Probably."


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
