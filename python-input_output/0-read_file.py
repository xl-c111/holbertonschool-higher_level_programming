#!/usr/bin/python3
"""
This module provides a utility function to read and print the content of a file
"""


def read_file(filename=""):
    """ Reads a text file (UTF-8) and prints its content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
