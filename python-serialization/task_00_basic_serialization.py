#!/usr/bin/python3
"""
This module provides functions for serializing Python objects to a JSON file
and deserializing Python objects from a JSON file.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python object to JSON and save it to a file."""
    with open(filename, "w") as f:
        return json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON data from a file and deserialize it to a Python object."""
    with open(filename, "r") as f:
        return json.load(f)
