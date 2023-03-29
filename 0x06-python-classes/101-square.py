#!/usr/bin/python3
"""my square module."""


class Square:
    """define a Square."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """property of the length of a side of square
        Raises:
            TypeError: if size is not an int.
            ValueError: if size is < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size of square
        Args:
            value: the size
        Raises:
                TypeError: if value is not int
                ValueError: if valie < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """returns the printed square with position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position
        Args:
            value: where
        Raises:
                TypeError: if not tuple, ints, positive
        Returns: the position
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not isinstance(value[0], int) or not isinstance(value[1], int) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ the area of square
        Returns:
            size * size
        """
        return self.__size ** 2

    def my_print(self):
        """print square."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """teach python to print the square my way"""
        s = ""
        if self.__size == 0:
            s += "\n"
        else:
            for i in range(self.__position[1]):
                s += "\n"
            for i in range(self.__size):
                s += " " * self.__position[0] + "#" * self.__size + "\n"
        return s[:-1]
