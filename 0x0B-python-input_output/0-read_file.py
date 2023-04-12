#!/usr/bin/python3

"""
This cotains module of read text fuction
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout

    """
    with open(filename, 'r', encoding='utf8') as file:
        print(file.read(), end="")
