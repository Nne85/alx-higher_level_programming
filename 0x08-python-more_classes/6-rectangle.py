#!/usr/bin/python3

"""
This module contains a class that defines a Rectangle with
private attribute width

"""


class Rectangle:
    """
    Defines a rectangle with a width and height.

        Attributes:
        number_of_instances: Counter for number of instances created
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

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """Returns the string representation \
                of the rectangle for recreation."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes the instance of the rectangle \
                and decrements the instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
