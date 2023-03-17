#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
    - a_dictionary: dictionary to be modified
    - key: key to be deleted, default is an empty string

    Return:
    - the modified dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
