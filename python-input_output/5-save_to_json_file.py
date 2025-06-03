#!/usr/bin/python3
"""
This module provides a function for saving Python objects to a file in JSON
format.
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
