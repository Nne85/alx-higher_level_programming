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
        self.__size = size

    @property
    def size(self):
        """
        retrieve the value of __size using the size method
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the value of __size using the same method.

                Parameters
        ----------
        size : int, optional
            the size of the square (default is 0)

        value: int
             the value of the size of square

        Raises
        ------
        TypeError
            If `size` is not an integer.
        ValueError
            If `size` is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns
        -------
        int
            the area of the square.

        """
        return self.__size ** 2
