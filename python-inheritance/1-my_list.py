#!/usr/bin/python3
"""
This module defines a MyList class, which extends the built-in list
with additional functionality.
"""


class MyList(list):
    """
    MyList is a subclass of the built-in list.
    It provides a method to print the list in sorted order without modifying
        the original list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
