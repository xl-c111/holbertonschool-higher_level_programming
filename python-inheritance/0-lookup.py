#!/usr/bin/python3
"""
This module provides a lookup() function to list attributes and methods
of an object.
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object.
    """
    return dir(obj)
