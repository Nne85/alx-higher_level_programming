#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initialize Rectangle instance"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def __str__(self):
        """Return string representation of Rectangle instance"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
