#!/usr/bin/python3
"""
This module defines a Student class that supports conversion to a dictionary
representation suitable for JSON serialization. The to_json method can return
either all attributes or only a specified subset.
"""


class Student:
    """Initialize a Student instance."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary containing attributes of the Student instance for
        JSON serialization.

        If 'attrs' is provided and is a list of strings, the returned
        dictionary will only include those attributes whose names are listed in
        'attrs' (and that actually exist on the object).

        If 'attrs' is not provided or is not a list of strings, all attributes
        of the Student instance will be included in the returned dictionary.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for
                                           attr in attrs):
            res = {}
            for attr in attrs:
                if hasattr(self, attr):
                    res[attr] = getattr(self, attr)
            return res
        return self.__dict__.copy()
