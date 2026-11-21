from __future__ import annotations
from .lesson_03 import is_image
import os


def list_files(folder: str) -> list[str]:
    """Return the sorted names of the files (not folders) directly inside folder."""
    names = []
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if os.path.isfile(path):
            names.append(name)
    names.sort()
    return names


def image_files(folder: str) -> list[str]:
    """Return the sorted names of the .exr and .dpx files directly inside folder, any case."""
    names = []
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if os.path.isfile(path) and is_image(name):
            names.append(name)
    names.sort()
    return names
