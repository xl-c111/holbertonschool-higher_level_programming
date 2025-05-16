#!/usr/bin/python3
"""
This module provides a simple function to print a full name.

The function `say_my_name` takes a first name and an optional last name
and prints them in the format: "My name is <first_name> <last_name>".

It validates that both arguments are strings. If either argument is not
a string, a TypeError is raised.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a message with the given first and last name.

    Args:
        first_name (str): The first name to print. Required.
        last_name (str, optional): The last name to print.
            Defaults to an empty string.
    Return:
        None
    Raises:
        TypeError: If `first_name` or `last_name` is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
