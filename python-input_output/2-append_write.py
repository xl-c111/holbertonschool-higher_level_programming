#!/usr/bin/python3
"""
This module provides a function to append a string to a text file (UTF-8)
and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8) and returns the
    number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        nb_characters_added = f.write(text)
    return nb_characters_added
