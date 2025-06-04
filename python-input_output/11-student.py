#!/usr/bin/python3
"""
This module defines a Student class with methods to serialize its attributes
to a dictionary and to update its attributes from a dictionary (typically from
JSON).
"""


class Student:
    """Represents a student with a first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance."""
        if isinstance(attrs, list) and all(isinstance(attr, str) for
                                           attr in attrs):
            return {attr: getattr(self, attr) for attr in hasattr(self, attr)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Updates or sets the instance's attributes using the key-value
        pairs from the provided dictionary.

        Args:
            json(dict): whose key-value pairs will be assigned as attributes
            to the instance.
        """
        # loop through key-value pairs in json dict
        for key, value in json.items():
            #
            setattr(self, key, value)


# workflow
"""
1, Using to_json() to export instance's attributes as a dict(often called a json dict). 
e.g.
s = Student("Tom", "Lee", 18)
print(s.to_json())                             # {'first_name': 'Tom', 'last_name': 'Lee', 'age': 18}
print(s.to_json(['first_name', 'age']))        # {'first_name': 'Tom', 'age': 18}

2, Using reload_from_json() to import or update instance's attributes. 
e.g. 
s = Student("Tom", "Lee", 18)
s.reload_from_json({'first_name': 'Alice', 'age': 25})
print(s.to_json())                             # {'first_name': 'Alice', 'last_name': 'Lee', 'age': 25}
"""
# setattr() syntax
"""
setattr(object, name, value)

object: The object whose attribute you want to set.
name: The attribute name (as a string).
value: The value to assign to the attribute.

"""
