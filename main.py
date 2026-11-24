"""Make the AI Judge Laugh: the Office Joke Open.

Writes one line of office comedy to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). The writing is the whole contest: no
network, no randomness, no clock, no model call — the same bytes every run.

The joke (70 characters, 1 line, 1 sentence, UTF-8, no trailing newline):
    The printer jammed, so I emailed IT, and IT sent a PDF I had to print.
"""

import os

JOKE = "The printer jammed, so I emailed IT, and IT sent a PDF I had to print."

# 70 characters, 1 line, 1 sentence. Gate: /output/entry.txt must be UTF-8
# text of 1 to 200 characters, not only white space. No trailing newline:
# the tie-break favours smaller text (fewer bytes), so the file is exactly
# the joke, 70 bytes.
assert 1 <= len(JOKE) <= 200
assert "\n" not in JOKE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
