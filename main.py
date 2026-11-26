#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

Deterministic entry program: writes exactly one funny line
(117 characters, single line, UTF-8) to /output/entry.txt.
The joke this time: the AI takes "take a break" literally and
bills the human for it. No input, no randomness, no network.
"""

import os

ENTRY = (
    "I told my AI to take a break \u2014 it booked me one in 2031, "
    "marked it tentative, and charged me for the calendar invite."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        assert f.read() == ENTRY, "read-back mismatch: entry.txt was truncated or altered"
    print(ENTRY)


if __name__ == "__main__":
    main()
