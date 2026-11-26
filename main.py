#!/usr/bin/env python3
"""Write the weirdest job title we can think of.

The title is one corporate-sounding job with a single hilariously
specific twist: a Senior Vice President whose whole job is apologizing
to printers. It sounds like a real job (grand title, real department
energy), the twist lands on the first read (everyone has fought a
printer), and it is short enough to take in at a glance. Well under
the 60-character cap.
"""

import os

TITLE = "Senior Vice President of Apologizing to Printers"

# The gate rejects anything outside 1-60 characters, so fail loudly here
# instead of shipping an entry the judge never sees. A job title is one
# line: a newline inside it would read as two lines, so reject that too.
# The gate also rejects whitespace-only text, so the title must survive
# a strip unchanged — no leading or trailing space may sneak in.
assert 1 <= len(TITLE) <= 60, f"title is {len(TITLE)} characters, gate needs 1-60"
assert "\n" not in TITLE, "job title must be a single line"
assert TITLE == TITLE.strip() and TITLE, "job title must not be blank or padded"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE)
    # Round-trip check: what the judge reads must be exactly the title,
    # byte for byte — no trailing newline, no extra whitespace.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == TITLE, "entry.txt does not match the title"
    print(TITLE)


if __name__ == "__main__":
    main()
