#!/usr/bin/python3
"""
A Student class that defines a Studen (module)
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize the instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of a Student instance"""
        return (self.__dict__)
