#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

Deterministic entry program: writes exactly one funny line
(120 characters, single line, UTF-8) to /output/entry.txt.
No input, no randomness, no network.
"""

import os

ENTRY = (
    "My AI assistant asked for a raise \u2014 I said it already has one: "
    "it lives rent-free in my head and on my electricity bill."
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
