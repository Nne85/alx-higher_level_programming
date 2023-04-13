#!/usr/bin/python3

"""
This contains a function to append text to a file
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8)

    Returns the number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
