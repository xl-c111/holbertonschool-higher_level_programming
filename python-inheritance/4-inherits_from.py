#!/usr/bin/python3
"""
This module provides a function to check whether an object is an instance
of a subclass (directly or indirectly) of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a subclass (directly or
    indirectly) of the specified class; otherwise, return False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
