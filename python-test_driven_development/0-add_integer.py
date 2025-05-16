#!/usr/bin/python3
"""
This module provides a function to add two integers.
It checks that inputs are either int or float types.
It raises a TypeError if inputs are invalid.
It returns the sum as an integer.
"""


def add_integer(a, b=98):
    """
    Adds two numbers after validating and converting them to integers.

    Parameters:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
        The sum of the two input values.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
