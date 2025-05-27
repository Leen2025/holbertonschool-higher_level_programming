#!/usr/bin/python3
"""Function to add attribute to an object if possible."""


def add_attribute(obj, attr_name, value):
    """Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which to add the attribute.
        attr_name: The name of the attribute to add.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
