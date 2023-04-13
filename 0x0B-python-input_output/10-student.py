#!/usr/bin/python3
"""
A Student class that defines a Studen (module)
"""


class Student:
    """
        A Student class that defines a Student
    """
    def __init__(self, first_name, last_name, age):
        """Initialize the instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return (new_dict)
