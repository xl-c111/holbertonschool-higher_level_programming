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

        Args:
            attrs(list): List of attribute names to include.
        Returns:
            dict: Dictionary containing the selected attributes and their values.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for
                                           attr in attrs):
            res = {}
            # loop through each attribute name in attrs
            for attr in attrs:
                # if self has this attribute. hasattr(obj, name)
                if hasattr(self, attr):
                    # get the value and add it to res
                    res[attr] = getattr(self, attr)
            return res
        # if return self.__dict__ directly, the caller receives a reference of internal dict.
        # if user modifies this dict, they will actually change the attributes of this dict.
        # By using .copy() any change made to the returned dict will not affect the original attributes.
        return self.__dict__.copy()


"""
hasattr(obj, name) checks if the obj has an attribute named "name"
getattr(obj, name) gets the value of the attribute named "name"
res["first_name"] = "Jack"
"""
