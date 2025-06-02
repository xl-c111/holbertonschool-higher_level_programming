#!/usr/bin/python3
"""
This module provides a function to write a string to a text file (UTF-8)
and return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number of
    characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        nb_characters = f.write(text)
    return nb_characters
