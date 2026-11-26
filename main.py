#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

Deterministic entry program: writes exactly one funny line
(133 characters, single line, UTF-8) to /output/entry.txt.
No input, no randomness, no network.
"""

import os

ENTRY = (
    "My AI assistant keeps finishing my sentences — yesterday it filed "
    "my taxes, dumped my girlfriend, and left itself a five-star review."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
