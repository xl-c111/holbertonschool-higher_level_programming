#!/usr/bin/python3
"""
This module provides a function for loading Python objects from a file
containing JSON data.
"""
import json


def load_from_json_file(filename):
    """Load a Python object from a file containing JSON data."""
    with open(filename, "r") as f:
        return json.load(f)
