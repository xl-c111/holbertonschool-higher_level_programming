#!/usr/bin/python3
"""This module provides a function to insert a line of text into a file
immediately after each line containing a specified search string."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a new string into a file immediately after each line containing
    a given search string."""

    output_lines = []

    with open(filename, "r") as f:

        # iterate through each line of file one by one
        for line in f:
            # add current line to the empty list, whether it matches or not
            output_lines.append(line)
            if search_string in line:
                output_lines.append(new_string)

    # open the file with write mode, it will overwrite the original file with new content
    with open(filename, "w") as f:
        f.writelines(output_lines)


"""
Syntax: file_obj.writelines(list_of_strings)

Function: write each string from the list to the file in sequence, with no automatic line breaks.
Note: writelines() does not automatically add a newline (\n) after each item.

file_obj: a file obj opened with open(), it must be in write mode
"""
