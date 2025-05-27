#!/usr/bin/python3
"""
Module: 7-base_geometry
Defines class BaseGeometry with area() and integer_validator()
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """area method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that 'value' is a positive integer

        Args:
            name (str): name of the variable
            value (any): value to validate

        Raises:
            TypeError: if value is not an int
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
