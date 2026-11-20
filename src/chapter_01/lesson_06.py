from __future__ import annotations


def missing_frames(expected: list[int], found: list[int]) -> list[int]:
    """Return the sorted frames in expected that are not in found."""
    return sorted(set(expected) - set(found))


def extra_frames(expected: list[int], found: list[int]) -> list[int]:
    """Return the sorted frames in found that are not in expected."""
    return sorted(set(found) - set(expected))
