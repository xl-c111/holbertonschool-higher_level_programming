#!/usr/bin/python3
"""
This module provides a function to print a square of size 'size' using
the '#' character.
It checks if size is a non-negative integer.
It raises TypeError if size is not an integer.
It raises ValueError if size is negative.
"""


def print_square(size):
    """
    Prints a square of size `size` using the '#' character.

    Args:
        size: is the size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
