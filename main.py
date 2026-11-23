#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry (program/v1).

Writes exactly one emoji to /output/entry.txt: U+1F604 GRINNING FACE WITH
SMILING EYES.

Why this one, against the judge's published brief:
- A big, genuine-looking smile: smiling eyes plus an open grin, the kind of
  face most likely to make a stranger smile back at first glance.
- Universal: no words, no irony, no in-joke; readable at any age, in any
  background.
- Chosen, not default: warmer and more exuberant than the plain 🙂 or 😊
  that first come to mind, while staying instantly readable.
- Right for a stranger: pure friendliness. No hearts, no hug, no kiss, so
  nothing intimate, flirtatious or sarcastic that would read oddly from
  someone unknown.

The entry is a single character, written as UTF-8 with no trailing newline,
well inside the gate's 1-to-8-character limit. No network, no secrets, no
files outside this repository: the emoji is a constant below.
"""

import os
import sys

# U+1F604 GRINNING FACE WITH SMILING EYES — the whole entry.
ENTRY = "\U0001F604"

OUTPUT_PATH = "/output/entry.txt"


def check_entry(text: str) -> bytes:
    """Validate the entry against the published gate, then encode it."""
    if len(text) < 1 or len(text) > 8:
        raise ValueError(f"entry must be 1-8 characters, got {len(text)}")
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if len(text) != 1:
        raise ValueError("entry must be exactly one emoji")
    encoded = text.encode("utf-8")
    if len(encoded) > 8:
        raise ValueError(f"entry must be at most 8 bytes, got {len(encoded)}")
    return encoded


def main() -> int:
    encoded = check_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)
    # Read it back and confirm the file holds exactly the entry, byte for byte.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != encoded:
        print(f"verification failed: {OUTPUT_PATH} does not match entry",
              file=sys.stderr)
        return 1
    decoded = written.decode("utf-8")
    print(f"wrote entry {decoded!r} "
          f"({len(decoded)} character, {len(written)} bytes) "
          f"to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
