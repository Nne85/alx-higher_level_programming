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

    def to_json(self, attrs=None):
        """Return a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    new_dict[attr] = self.__dict__[attr]
            return (new_dict)

    def reload_from_json(self, json):
        """
        """
        for key, value in json.items():
            setattr(self, key, value)
