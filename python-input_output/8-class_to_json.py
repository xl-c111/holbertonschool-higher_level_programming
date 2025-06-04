#!/usr/bin/python3
"""This module provides a function that converts class object into its
JSON representation"""


def class_to_json(obj):
    """
    Returns a dictionary description of a class instance suitable for
    JSON serialization.

    Args:
        obj: the class instance whose attributes will be converted.
    Returns:
        dict: a dictionary containing all serializable attributes of the object
    """
    return obj.__dict__
