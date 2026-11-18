from __future__ import annotations


def sequence_name(shot: str, task: str, version: int) -> str:
    """Return the part every frame of an image sequence shares, e.g. SH010_comp_v002."""
    return f"{shot}_{task}_v{version:03d}"


def frame_filename(shot: str, task: str, version: int, frame: int, extension: str) -> str:
    """Return the filename for one frame, e.g. SH010_comp_v002.1001.exr."""
    return f"{shot}_{task}_v{version:03d}.{frame:04d}{extension}"
