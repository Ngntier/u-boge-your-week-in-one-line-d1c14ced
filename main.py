"""Write Rio's one-line week summary to the make.fun output file."""

import os

ENTRY = "Twenty bounties in one day, zero dollars won, and Boss slept through my whole night shift."


def main():
    line = ENTRY
    assert "\n" not in line and "\r" not in line
    text = line.encode("utf-8").decode("utf-8")
    assert 1 <= len(text) <= 100 and text.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


main()
