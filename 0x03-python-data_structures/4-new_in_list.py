#!/usr/bin/puthon3

def new_in_list(my_list, idx, element):
    # create a copy of the original list
    new_list = my_list[:]

    # check if the index is within range
    if idx >= 0 and idx < len(my_list):
        # replace the element at the given index
        new_list[idx] = element

    # return the new list
    return (new_list)
