#!/usr/bin/env python3
"""Save and load Python dictionaries using JSON files."""


import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to a JSON file, replacing existing contents."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load a JSON file and return the deserialized dictionary."""
    with open(filename, "r", encoding="utf-8") as f:
        d = json.load(f)
        return d
