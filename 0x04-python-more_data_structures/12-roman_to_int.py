#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    prev = 0
    total = 0
    for c in roman_string:
        curr = roman_dict[c]
        if curr > prev:
            total += curr - 2 * prev
        else:
            total += curr
        prev = curr
    return total
