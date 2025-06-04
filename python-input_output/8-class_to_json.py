#!/usr/bin/python3
"""This module provides a function that converts class object into its
JSON representation"""
import json


def class_to_json(obj):
    """ Convert a class object to a JSON string."""
    return json.dumps(obj.__dict__)
