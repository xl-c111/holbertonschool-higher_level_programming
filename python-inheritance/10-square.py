#!/usr/bin/python3
"""
this module defines a BeseGeometry class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square is a subclass of Rectangle that represents a square shape.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Return the area of the square.
        """
        # when call super().area(), it'll look up the inheritance chain
        # super().area() inside Square will call the Rectangle version, not the
        # BaseGeometry version
        return self.__size * self.__size
