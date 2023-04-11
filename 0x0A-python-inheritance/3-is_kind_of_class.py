#!/usr/bin/python3
"""
Module for is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    checksbif the object is an instance of class.
    Args:
    obj(object) to check
    a_class(test object) to check
    Return: True or False
    """
    return isinstance(obj, a_class)
