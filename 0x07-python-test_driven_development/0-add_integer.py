#!/usr/bin/python3

"""
This module conatins the function for strictly adding 2 numbers
of data type int or floats together, any other data type is regarded
as invalid with exceptions being raise signifying what caused the error.

"""


def add_integer(a, b=98):
    """Add 2 integers.

    Args:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or a float.

    """
    data = (int, float)

    if not isinstance(a, (int, data)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, data)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
