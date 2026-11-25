#!/usr/bin/env python3
"""Two Days of Quiet Dread — writes one line to /output/entry.txt.

The line is a single code review comment of at most 140 characters that
approves a pull request while carrying quiet existential dread. It approves
in the first word, keeps the dread flat and understated — no exclamation,
no melodrama — and lets the laugh come from the dread itself: the reviewer
already knows future-them will be the one stuck explaining this merge.
"""

import os

LINE = "Approved. Clean diff, green tests, and the quiet certainty that future me will be the one explaining this merge."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
