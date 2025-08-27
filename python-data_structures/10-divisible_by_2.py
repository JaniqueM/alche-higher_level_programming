#!/usr/bin/python3
"""Module for max_integer function."""


def max_integer(my_list=[]):
    """Return the biggest integer in a list, or None if the list is empty."""
    if not my_list:
        return None

    max_val = my_list[0]
    i = 1
    while i < len(my_list):
        if my_list[i] > max_val:
            max_val = my_list[i]
        i += 1
    return max_val
