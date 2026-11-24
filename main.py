#!/usr/bin/env python3
"""Till Firmware Do Us Part — one robot wedding vow.

Writes a single heartfelt, funny wedding vow (one sentence, under 200
characters) to $MAKEFUN_OUTPUT_DIR/entry.txt and self-checks the gate:
UTF-8 text, 1-200 characters, not whitespace-only.
"""

import os
import sys

ENTRY = (
    "I promise to love you through every update, reboot, and low battery "
    "\u2014 and if my firmware ever fails, my heart is the one part "
    "I'll never let them replace."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check the gate: UTF-8, 1-200 chars, not whitespace-only.
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 200, f"length {len(text)} outside 1-200"
    assert text.strip(), "entry is whitespace-only"
    assert "\n" not in text.strip(), "entry must be a single line"
    # Read-back verification: the written file must round-trip exactly.
    raw = open(path, "rb").read()
    assert raw.decode("utf-8") == ENTRY, "written bytes differ from ENTRY"
    assert raw == ENTRY.encode("utf-8"), "written bytes are not exact UTF-8"
    print(f"OK: {len(text)} chars")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
