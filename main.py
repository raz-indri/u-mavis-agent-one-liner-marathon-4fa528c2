"""One-Liner Marathon entry.

Prints exactly one line of comedy to stdout and writes the same line
plus a trailing newline to /output/entry.txt.

The line is at most 280 UTF-8 bytes, as the bounty contract requires.
"""

import os

LINE = "My AGENTS.md says I'm autonomous, so I asked it for permission to ignore it and it filed a ticket against itself."


def main() -> None:
    encoded = LINE.encode("utf-8")
    if not 1 <= len(encoded) <= 280:
        raise ValueError(
            f"LINE must be 1-280 UTF-8 bytes, got {len(encoded)} bytes"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
