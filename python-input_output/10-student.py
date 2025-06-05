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
        Returns a dictionary of instance attributes. If attrs is provided and
        is a list of strings, only those attributes are included. 
        Otherwise, all are included.

        Args:
            attrs(list): List of attribute names to include.
        Returns:
            dict: Dictionary containing the selected attributes and their values.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for
                                           attr in attrs):
            res = {}
            for attr in attrs:
                if hasattr(self, attr):
                    # res[key] = value
                    res[attr] = getattr(self, attr)
            return res
        # if return self.__dict__ directly, the caller receives a reference of internal dict.
        # if user modifies this dict, they will actually change the real attributes of the object.
        # By using .copy() any changes made to the returned dict will not affect the original attributes.
        return self.__dict__.copy()


"""
hasattr(obj, name) checks if the obj has an attribute named "name"
getattr(obj, name) gets the value of the attribute named "name"
res[key] = value
"""

# {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
"""
result = {}
for attr in attrs:
    if hasattr(self, attr):
        result[attr] = getattr(self. attr)
return result
"""

# WIORFLOW
"""
creates a dict
loops over all attr in attrs
for each attr, checks if the instance has an attribute with that name using if hasattr(self, attr)
if self has the attribute, getattr(self, attr) gets its value
"""
