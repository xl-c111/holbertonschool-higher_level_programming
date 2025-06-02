#!/usr/bin/python3
"""
This module provides a function to convert a JSON string to its corresponding
Python object using the standard library `json` module.
"""
import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string."""
    obj = json.loads(my_str)
    return obj
