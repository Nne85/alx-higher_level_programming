#!/usr/bin/python3
""" docstring for the module """


import math


class MagicClass:
    """set up the magic"""

    def __init__(self, radius=0):
        """ writing another docstring """
        self.__radius = 0
        self.radius = radius

    def area(self):
        """ writing another docstring """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ writing another docstring """
        return 2 * math.pi * self.__radius

    @property
    def radius(self):
        """ writing another docstring """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """ writing another docstring """
        if type(value) not in [int, float]:
            raise TypeError("radius must be a number")
        if value < 0:
            raise ValueError("radius must be >= 0")
        self.__radius = value
