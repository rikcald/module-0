from __future__ import annotations

from typing import Any
import json


def save_json(data: Any, path: str) -> None:
    """Write data to path as UTF-8 JSON, indented by 2 spaces."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_json(path: str) -> Any:
    """Return the data from a JSON file."""
    with open(path, encoding="utf-8") as file:
        loaded = json.load(file)
    return loaded
