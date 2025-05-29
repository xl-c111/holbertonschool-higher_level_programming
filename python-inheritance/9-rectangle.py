#!/usr/bin/python3
"""
this module defines a BeseGeometry class.
"""


class BaseGeometry:
    """
    A base class for geometry-related operations.
    """

    def area(self):
        """
        Raise an Exception to indicate that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate the value
        """
        # isinstance(value, int) will treat bool values (True/False) as int
        # because bool is a subclass of int in Python
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
        # BaseGeometry.integer_validator(self, "width", width)
        # super().integer_validator("width", width)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        in child class, override the area(self) method with the actual
        implementation
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
