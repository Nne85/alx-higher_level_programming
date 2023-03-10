#!/usr/bin/python3
from magic_calculation import add, sub

add = magic_calculation_102.add
sub = magic_calculation_102.sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
