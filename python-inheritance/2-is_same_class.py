#!/usr/bin/python3
"""
this module provides a function to check whether the object is exactly an
instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class;
    otherwise False
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    """
    if type(obj) is a_class:
        return True
    return False
