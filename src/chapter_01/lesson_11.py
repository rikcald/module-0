from __future__ import annotations
from .lesson_03 import is_image
import os
import sys


def main(args: list[str]) -> int:
    """Print how many image files a folder holds; return 0, or 2 for bad input."""
    if len(args) != 1:
        print("usage: count-frames FOLDER")
        return 2
    if not os.path.isdir(args[0]):
        print(f"error: {args[0]} is not a folder")
        return 2
    n = 0
    for name in os.listdir(args[0]):
        path = os.path.join(args[0], name)
        if os.path.isfile(path) and is_image(name):
            n += 1
    print(f"{n} image files")
    return 0


# TODO: the guard: when this file is run directly, unpack sys.argv and exit with main(args)
if __name__ == "__main__":
    script, *args = sys.argv
    sys.exit(main(args))
