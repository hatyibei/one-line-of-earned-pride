"""Entry for make.fun's "One Line of Earned Pride" bounty.

Writes one line -- a quiet, earned moment of pride for someone in a
concrete scene -- to /output/entry.txt.
"""

import os

TEXT = (
    "For six years the night janitor taught himself piano on the lobby Steinway after "
    "his shift; tonight he played it at his daughter's recital, and nobody checked a phone."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
