#!/usr/bin/python3
"""
This module provides a function to print a formatted text with
two newlines after each occurrence of '.', '?' or ':'.

It ensures that each printed line has no leading or trailing spaces.
"""


def text_indentation(text):
    """
    Prints a text with two newlines after each '.', '?' or ':' character.

    The function removes any leading or trailing whitespace from each printed
    line. It skips any spaces immediately following '.', '?' or ':' to prevent
    leading spaces in the next printed segment.

    Args:
        Test: the given test.
    Raises:
        TypeError: If the input is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    temp = ""
    i = 0
    while i < len(text):
        temp += text[i]
        if text[i] in ".?:":
            print(temp.strip())
            print()
            temp = ""
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    if temp.strip():
        print(temp.strip(), end="")
