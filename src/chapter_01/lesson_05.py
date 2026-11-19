from __future__ import annotations


def frame_list(first: int, last: int) -> list[int]:
    """Return every frame from first to last, including last; empty when last is before first."""
    return [frame for frame in range(first, last + 1)] if first <= last else []


def expected_names(sequence: str, first: int, last: int, extension: str) -> list[str]:
    """Return every filename of the image sequence, in frame order, frames padded to 4 digits."""
    return [f"{sequence}.{frame:04d}{extension}" for frame in range(first, last + 1)] if first <= last else []
