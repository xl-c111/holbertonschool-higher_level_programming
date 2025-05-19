#!/usr/bin/python3
"""
This module provides a simple implementation of an empty Square Class
with validated size attribute.
"""


class Square:
    """
    Represents a square with given size.

    Attributes
        __size: integer - the length of sides of square.

    Methods
        __init__(size=0): initializes a Square instance with a given size.

    Returns:
        the area of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square with given size.

        Arguments
            size : int - The length of the sides of the square(default is 0).

        """
        # Use self.size = size inside __init__ to trigger setter to validate
        # and set value
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        get the size of the square.
        Returns
            int: the size of the square.
        """
        # Use self.__size inside property methods and internal methods
        # to access the stored actual value.
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size of the square.

        Parameters:
            value: int - the size of the square.

        Raises
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        get the current position of the square.

        Returns
            tuple of int: the position offset as a tuple(x, y).
            x is the number of spaces to skip before each line.
            y is the number of blank lines to skip before the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        set the positionz of the square.

        Parameters:
            value: tuple of two non-negative integers(x, y)
                x specifies the horizontal space offset.
                y specifies the number of blank lines above the square.

        Raises:
            TypeError: if the value is not a tuple of two non-negative ints

        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        return the area of the square.

        Returns:
            int - the area of the square.
        """

        return self.__size * self.__size

    def my_print(self):
        """
        prints in stdout the square with the character #.
        If size is 0, prints an empty line.
        The number of blank lines printed above the square is
            determinded by position[1].
        The number of spaces printed before each line is determinded by
            position[0].
        """
        if self.__size == 0:
            print()
            return
        if self.position[1] > 0:
            print()
        i = 0
        while i < self.__size:
            print("{}{}".format((' ' * self.position[0]), ('#' * self.__size)))
            i += 1
