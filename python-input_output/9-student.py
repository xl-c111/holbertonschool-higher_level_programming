#!/usr/bin/python3
"""
This module defines a Student class with a method for JSON serialization.
"""


class Student:
    """Initialize a Student instance."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of the Student instance
        for JSON serialization."""
        return self.__dict__
