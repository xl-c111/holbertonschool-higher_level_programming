#!/usr/bin/python3
"""
Add two integers, casting floats to ints if needed.
Raises TypeError if inputs are not int or float.
Returns the sum as an integer.
"""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
