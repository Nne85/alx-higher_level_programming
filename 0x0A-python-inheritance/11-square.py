#!/usr/bin/python3
"""
This module defines a Square class that inherits from the Rectangle class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes an instance of Square with a given size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the Square instance
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        Returns the square description
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
