#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file"""

import sys
import os.path
from os import path
from json import dump, load
from typing import List


def save_to_json_file(my_obj: List, filename: str):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as file:
        dump(my_obj, file)


def load_from_json_file(filename: str) -> List:
    """creates an Object from a “JSON file”"""
    if path.exists(filename):
        with open(filename, mode="r", encoding="utf-8") as file:
            return load(file)
    else:
        return []


if __name__ == "__main__":
    args = sys.argv[1:]
    my_list = load_from_json_file("add_item.json")
    my_list += args
    save_to_json_file(my_list, "add_item.json")
