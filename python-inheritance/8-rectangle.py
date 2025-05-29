#!/usr/bin/python3
"""
this module defines a BeseGeometry class.
# """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle is a subclass of BaseGeometry that represents a rectangle shape.
    The Rectangle class validates that both width and height are positive
    integers using the integer_validator method from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
