#!/usr/bin/python3

"""
This module defines a function that writes an Object to a text file,
using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """write the JSON representation of my_obj to the file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
