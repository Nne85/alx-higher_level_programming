#!/usr/bin/python3

"""
This module contains a class that defines a Rectangle with
private attribute width

"""


class Rectangle:
    """A Rectangle class


    Attributes:
        number_of_instances: Counter for number of instances created
        or deleted
        print_symbol: Used as symbol for string representation
        width: The width of rectangle
        height: The height of rectangle
        __init__(self, width=0, height=0)
        area: The rectangle area
        perimeter: The rectangle perimeter
        __str__: Print the rectangle
        __repr__: Return string representation of the rectangle
        __del__: Print delete message
    Raise:
        TypeError: width must be an integer
        ValueError: width must be >= 0
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle"""

        if self.width == 0 or self.height == 0:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") * self.height)\
            .rstrip()

    def __repr__(self):
        """Return a string representation of the rectangle"""

        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Delete a rectangle instance"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
