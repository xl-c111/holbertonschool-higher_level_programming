#!/usr/bin/python3
"""
This module defines the MyInt class, which inherits from int and
inverts the equality operators.
"""


class MyInt(int):
    """
    MyInt is a subclass of int with inverted equality (==) and
    inequality (!=) operators.
    """
    # __new__ is called before __init__, is reponsible for creating and
    # returning a new object
    def __new__(cls, value):
        """
        Create a new instance of MyInt with the given integer value.
        """
        # return super().__new__(cls, value) calls the parent class (int)'s
        # __new__ method, passing in the cls and value to be stored.
        # it guarantees that the new object behaves like an int
        return super().__new__(cls, value)

    # custom methods
    def __eq__(self, other):
        """Invert the behavior of the equality operator (==)."""
        return int(self) != int(other)

    # custom methods
    def __ne__(self, other):
        """Invert the behavior of the inequality operator (!=)."""
        return int(self) == int(other)


"""
for immutable types like int, str, tuple, object creation happens in __new__,
    not in __init__
if you want to custmize how an immutable object is created, you must override
    __new__
"""
