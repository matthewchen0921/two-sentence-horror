#!/usr/bin/env python3
"""Two-Sentence Horror — "The Quiet Tenant Downstairs".

Writes one invented two-sentence horror story (under the 400-character
cap) to /output/entry.txt.

The story is entirely invented: no real incident, no real person.
"""

import os

STORY = (
    "The woman downstairs is the quietest tenant I have ever had \u2014 "
    "in six months, I have never heard a single footstep from her flat. "
    "This morning I found a trail of dusty footprints across my bedroom "
    "ceiling, leading away from the space above my pillow."
)


def main() -> None:
    # The gate: UTF-8 text of 1 to 400 characters, exactly two sentences.
    assert STORY.count(".") == 2, "story must be exactly two sentences"
    assert 1 <= len(STORY) <= 400, "story must be 1-400 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
