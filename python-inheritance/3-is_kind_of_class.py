#!/usr/bin/python3
"""
this module provides a function that checks whether the object is an instance
of a specific class or if the object is an instance of a class that inherited
from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    return true if an the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class
    otherwise False
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    """
    if isinstance(obj, a_class):
        return True
    return False
