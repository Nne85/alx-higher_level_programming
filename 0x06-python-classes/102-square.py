#!/usr/bin/python3
"""
This module defines a class Square
"""


class Square:
    """
    This class defines a square
    """

    def __init__(self, size=0):
        """
        Initializes a square
        """
        self.size = size

    @property
    def size(self):
        """
        Gets the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares two squares
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares two squares
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compares two squares
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares two squares
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compares two squares
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares two squares
        """
        return self.area() >= other.area()
