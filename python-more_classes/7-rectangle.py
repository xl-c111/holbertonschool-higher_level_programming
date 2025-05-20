#!/usr/bin/python3
"""
This module provideds a simple implementation of a rectangle Class.
"""


class Rectangle:
    """
    Represents a rectangle with given width and height.
    Increments the number_of_instances class attribute.

    Class Attributes
    number_of_instances : int - The number of Rectangle instances currently
                          alive.
    print_symbol : str - The symbol used for string representation of the
                   rectangle(default '#')

    Instance Attributes
        __width: int - the width of the rectangle
        __height: int - the height of the rectangle

    Methods
        __init__(): initializes an instance of the rectangle class.
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
        __str__(): Returns the string representation of the rectangle using
                   print_symbol.
        __repr__(): Returns a string that can recreate the Rectangle instance.
        my_print(): Prints the rectangle using print_symbol.
        __del__(): Handles object deletion and decrements number_of_instances.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle with given size.

        Arguments
            width : int - the width of the rectangle (defeult 0)
            height: int - the height of the rectangle (default 0)

        Side Effects
            - Increments the class attribute `number_of_instances` by 1.
            - Sets the instance's `print_symbol` to the class attribute
                `print_symbol`.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

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

    def area(self):
        """
        gets the area of the rectangle.

        Returns
            int - the area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """
        gets the perimeter of the rectangle.

        Returns
            0 if width or height equals to 0.
            int - the perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        gets a string that visually represents a rectangle, with '#'

        Returns
            empty string if height or width equals to 0.
            str: The square as a formatted string.
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        result = []
        line = str(self.print_symbol * self.width)
        for i in range(self.height):
            result.append(line)
        return "\n".join(result)

    def __repr__(self):
        """
        Returns a string representation of the Rectangle instance that can be
        used to recreate the object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def my_print(self):
        """
        prints a string with '#', it internally calls the __str__() method to
        generate the formatted string.
        """
        print(self.__str__())

    def __del__(self):
        """
        called when the Rectangle instance is about to be deleted.
        decrements the class variable number_of_instances and prints a message
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
