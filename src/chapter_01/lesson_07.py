from __future__ import annotations


def sort_by_frame(names: list[str]) -> list[str]:
    """Return a new list of frame filenames sorted by frame number."""
    return sorted(names, key=lambda name: int(name.rsplit(".", 2)[1]))


def format_run(start: int, end: int) -> str:
    """Return "1004" for a single frame, or "1001-1004" for a range."""
    return f"{start}-{end}" if end > start else str(start)
