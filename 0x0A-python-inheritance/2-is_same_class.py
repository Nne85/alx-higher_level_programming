#!/usr/bin/python3

"""
is_same_class module
"""


def is_same_class(obj, a_class):
    """
    instance of the class
    Args:
        obj(object) to be checked
        a_class(class) to be checked
    Return: either True or False
    """
    return type(obj) == a_class
