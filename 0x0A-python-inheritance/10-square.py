#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle (9-rectangle.py).
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square object."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return an informal and nicely printable string representation."""
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Return the area of the square."""
        return (self.__size ** 2)
