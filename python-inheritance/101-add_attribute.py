#!/usr/bin/python3
"""
This module provides a function to add a new attribute to an object
if possible.
"""


def add_attribute(obj, attr, value):
    """
    Add a new attribute to an object if possible.

    Args:
        obj: The object to which to add the attribute.
        attr: The name of the new attribute.
        value: The value to set for the new attribute.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    # check if the object has a __dict__ or not, if so, by using __dict__ to add or modify attributes
    if hasattr(obj, "__dict__"):
        # using __dict__ to add attribute, obj.__dict__[key] = value
        # using __dict__ to update attribute, obj.__dict__[key] = new_value
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")


"""
Syntax: hasattr(obj, attr)

obj: the object whose attributes has to be checked
attr: the attribute need to be checked
"""
