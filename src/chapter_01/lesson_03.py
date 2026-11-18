from __future__ import annotations


def is_image(name: str) -> bool:
    """Return True for .exr and .dpx files in any letter case."""
    return name.lower().endswith((".exr", ".dpx"))


def split_frame_name(name: str) -> dict[str, str] | None:
    """Return sequence, frame, and extension of an image named SEQUENCE.FRAME.ext, or None."""
    split = name.rsplit(".", 2)
    if not name.lower().endswith((".exr", ".dpx")) or len(split) < 3:
        return None
    return {"sequence": split[0], "frame": split[1], "extension": "." + split[2]}
