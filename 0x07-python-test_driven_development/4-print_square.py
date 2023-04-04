#!/usr/bin/python3
"""
This module contain a function that prints a square
"""


def print_square(size):
    """
    Print a square of size `size` with the character #.

    Args:
        size (int): the size length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
