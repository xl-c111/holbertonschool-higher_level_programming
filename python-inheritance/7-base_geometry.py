#!/usr/bin/python3
"""
this module defines a BeseGeometry class.
"""


class BaseGeometry:
    """
    A base class for geometry-related operations.

    Methods:
        area(self): Raises an Exception indicating that the method is not
        implemented.
    """

    def area(self):
        """
        Raise an Exception to indicate that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate the value
        Args:
        name (str): The name of the value (used in the exception message).
        value: The value to validate.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to 0.
        """
        # isinstance(value, int) will treat bool values (True/False) as int
        # because bool is a subclass of int in Python
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
