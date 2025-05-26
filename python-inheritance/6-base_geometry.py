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
