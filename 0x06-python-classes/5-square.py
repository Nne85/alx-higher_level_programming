#!/usr/bin/python3

"""
This module contains function that define a square class

Function:
    size: calculate the area of a square
"""


class Square:
    """
    Square class represents a square.

    Private instance attribute:
        __size: integer, size of the square.

    Methods:
        def __init__(self, size=0): Constructs a Square object.
        def size(self): Getter method to retrieve __size attribute.
        def size(self, value): Setter method to set __size attribute.
        def area(self): Returns the area of the square.
        def my_print(self): Prints the square with '#' character.
    """

    def __init__(self, size=0):
        """
        Constructs a Square instance.

        Args:
            size: (int) Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method to retrieve __size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set __size attribute.

        Args:
            value: (int) Value to set __size attribute to.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            (int) The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with '#' character.

        If size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
