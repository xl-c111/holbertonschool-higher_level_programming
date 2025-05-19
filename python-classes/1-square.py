#!/usr/bin/python3
"""
This module provides a simple implementation of an empty Square Class
with size attribute.
"""


class Square:
    """
    Represents a square with given size.

    Attributes
        _size: integer or float - the length of sides of square.

    Methods
        __init__(size): initializes a Square instance with a given size.
    """

    def __init__(self, size):
        """
        Initializes a Square with given size.

        Arguments
            size : int or float - The length of the sides of the square.


        """
        self.__size = size
