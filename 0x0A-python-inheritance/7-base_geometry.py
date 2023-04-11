#!/usr/bin/python3
"""
This is a module for BaseGeometry class.
"""


class BaseGeometry:
    """Represents a base geometry."""

    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.

        Args:
        name (str): The name.
        value (int): The value.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
