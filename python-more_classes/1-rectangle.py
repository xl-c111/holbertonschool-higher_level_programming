#!/usr/bin/python3
"""
This module provideds a simple implementation of a rectangle Class.
"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes
        __width: int - the width of the rectangle
        __height: int - the height of the rectangle

    Methods
        __init__(): initializes an instance of the rectangle class.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle with given size.

        Arguments
            width : int - the width of the rectangle (defeult 0)
            height: int - the height of the rectangle (default 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        gets the width of rectangle.

        Returns
            int - The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of rectangle with validation.

        Parameters:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        gets the height of rectangle.

        Returns
            int - The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of rectangle with validation.

        Parameters:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
