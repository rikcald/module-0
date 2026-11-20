from __future__ import annotations


def group_by_sequence(names: list[str]) -> dict[str, list[int]]:
    """Return each image sequence with its sorted frames, each listed once; skip non-images and non-digit frames."""

    groups = {}
    for name in names:
        split = name.rsplit(".", 2)
        if not name.lower().endswith((".exr", ".dpx")) or len(split) < 3 or not split[1].isdigit():
            continue

        key = f"{split[0]}.{split[2]}"
        if key not in groups:
            groups[key] = []

        if int(split[1]) not in groups[key]:
            groups[key].append(int(split[1]))

    for key in groups:
        groups[key].sort()
    return groups
