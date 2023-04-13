#!/usr/bin/python3

"""
This module contains a function that returns an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    Takes a string argument and returns the corresponding
    Python data structure
    """
    return json.loads(my_str)
