#!/usr/bin/python3
"""This module provides a function for converting Python objects to their JSON
string representation using the standard library `json` module."""

import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object."""
    obj = json.dumps(my_obj)
    return obj
