#!/usr/bin/python3

"""
inherits_from module
"""


def inherits_from(obj, a_class):
    """
    checks instance of a class inherited.
    Args:
    obj(object) checks the object
    a_class(another object) checks another object
    Return: True or False
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
