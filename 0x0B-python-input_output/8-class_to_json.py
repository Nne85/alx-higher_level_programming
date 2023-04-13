#!/usr/bin/python3
"""
This module defines a function that returns a dictionary
description with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns a dictionary representation of an instance of a class,
    that can be serialized to JSON.

    Args:
        obj (object): instance of a class with serializable attributes

    Returns:
        dict: dictionary representation of the object
    """
    return (obj.__dict__)
