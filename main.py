#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut.

Writes the GPS's own excuse, in its own voice, for sending the driver
down the wrong road, to /output/entry.txt. One line, plain text.
"""

import os

LINE = "The map said the lake was a shortcut. I just read it out loud \u2014 you\u2019re the one who thought a road could swim."


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
