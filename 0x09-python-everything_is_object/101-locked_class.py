#!/usr/bin/python3
"""This module defines a locked class"""


class LockedClass:
    """
    This only allows instantiation of an attribute called first_name
    """

    __slots__ = ["first_name"]
