#!/usr/bin/env python3
""" Module containing the Base class """


class Base:
    """ Base class for all other classes in this project

    Attributes:

            Fields:
                __nb_objects
                id: Public instance attribute
            Methods:
                __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
