#!/usr/bin/python3
"""This module provides a function to insert a line of text into a file
immediately after each line containing a specified search string."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a new string into a file immediately after each line containing
    a given search string."""

    output_lines = []

    with open(filename, "r") as f:
        for line in f:
            output_lines.append(line)
            if search_string in line:
                output_lines.append(new_string)

    with open(filename, "w") as f:
        f.writelines(output_lines)
