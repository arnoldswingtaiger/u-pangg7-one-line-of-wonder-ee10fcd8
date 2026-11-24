"""One Line of Wonder — a make.fun bounty entry.

Writes a single line of text, written to stir wonder, to
/output/entry.txt. Python 3.13 standard library only: no network,
no input, no randomness.
"""

import os

ENTRY = (
    "Somewhere above us right now, a satellite older than you is still "
    "singing its position into the dark, waiting for anyone at all to listen."
)


def main() -> None:
    # One line, written exactly as given: 138 characters plus a newline.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
