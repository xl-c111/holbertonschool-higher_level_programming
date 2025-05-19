#!/usr/bin/python3
"""
This module provides a simple implementation of an empty Square Class
with validated size attribute.
"""


class Square:
    """
    Represents a square with given size.

    Attributes
        _size: integer or float - the length of sides of square.

    Methods
        __init__(size=0): initializes a Square instance with a given size.
    """

    def __init__(self, size=0):
        """
        Initializes a Square with given size.

        Arguments
            size : int or float - The length of the sides of the square.

        Raises
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self._size = size
