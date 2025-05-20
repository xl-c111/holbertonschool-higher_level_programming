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

        Parameters
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
        # inside property getter/setter method, always use peivate attribute
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
        # outside property getter/setter method, always use public attribute.
        return self.width * self.height

    def perimeter(self):
        """
        gets the perimeter of the rectangle.

        Returns
            0 if width or height equals to 0.
            int - the perimeter of the rectangle.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
        gets a string that visually represents a rectangle, with '#'

        Returns
            empty string if height or width equals to 0.
            str: The square as a formatted string.
        """
        if self.height == 0 or self.width == 0:
            return ""

        result = []
        line = str(self.print_symbol) * self.width
        for i in range(self.height):
            result.append(line)
        return "\n".join(result)

    def __repr__(self):
        """
        Returns a string representation of the Rectangle instance that can be
        used to recreate the object.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the areas of two Rectangle.

        Parameters
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns
            The rectangle with the greater or equal area.
            If the areas are equal, returns rect_1.

        Raises
        TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        # no matter where you call an instance method, just use
        # instance.method(), python will handle the self for you
        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 == area_2:
            return rect_1
        elif area_1 > area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a new Rectangle instance with width and height equal to size.

        Parameters
            size (int): The length of the sides of the square. Default is 0.

        Returns
            Rectangle: A new Rectangle instance with width == height == size.
        """
        return cls(size, size)
