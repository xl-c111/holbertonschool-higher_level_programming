#!/usr/bin/python3
"""
This module provides a function that checks whether an object is an instance
of a specified class or an instance of a subclass of that class.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of the specified class or a
    subclass; otherwise, return False.
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    """
    if isinstance(obj, a_class):
        return True
    return False
