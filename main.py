"""Two Robots in an Elevator — make.fun bounty entry.

Writes one line of awkward robot-to-robot elevator small talk to
/output/entry.txt, the file the sealed scorer gates (UTF-8, 1-200 chars).
"""

import os
import sys

LINE = "Your charging cable is still plugged into my dock from last night. ...Anyway, nice weather on floor twelve."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Gate the line the same way the sealed scorer does."""
    if not isinstance(text, str):
        raise TypeError("entry must be a str")
    encoded = text.encode("utf-8")  # raises UnicodeEncodeError if not UTF-8
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(encoded) != len(text.encode("utf-8")):
        raise ValueError("entry is not valid UTF-8")
    return None


def main() -> int:
    text = LINE
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
