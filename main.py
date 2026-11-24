#!/usr/bin/env python3
"""One sentence pitching a bizarre startup idea that actually sells.

Writes the sentence to /output/entry.txt. Gate: UTF-8 text, 1-200 chars,
not only whitespace, single sentence.
"""

LINE = (
    "Rent-a-Grandma: lonely city workers pay retired grandmothers by the hour "
    "to scold them, feed them soup, and call their mothers to say they're "
    "eating fine."
)

MAX_CHARS = 200


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    assert LINE.count("\n") == 0, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
