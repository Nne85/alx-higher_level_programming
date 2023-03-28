#!/usr/bin/python3

"""
This module contains function that define a square class

Function:
    size: calculate the area of a square
"""

class Square:
    """
    A class representing a square.

    Attributes:
    __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        __init__(self, size): Initializes a new instance of the Square class with the given size parameter.
        """
        self.__size = size
