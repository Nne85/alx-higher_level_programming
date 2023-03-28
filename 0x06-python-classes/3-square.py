#!/usr/bin/python3

"""
This module contains function that define a square class

Function:
    size: calculate the area of a square
"""


class Square:
    """
    A class used to represent a Square.

    ...

    Attributes
    ----------
    __size : int
        the size of the square (private).

    Methods
    -------
    area():
        Computes the area of the square.

    """

    def __init__(self, size=0):
        """
        Constructs all the necessary attributes for the Square object.

        Parameters
        ----------
        size : int, optional
            the size of the square (default is 0)

        Raises
        ------
        TypeError
            If `size` is not an integer.
        ValueError
            If `size` is less than 0.

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns
        -------
        int
            the area of the square.

        """
        return self.__size ** 2
