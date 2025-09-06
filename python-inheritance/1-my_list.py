#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list and
adds a public method to print the list in sorted order.
"""

class MyList(list):
    """
    MyList class inherits from the built-in list and provides
    an additional method to print the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending order.
        Assumes all elements are integers.
        """
        print(sorted(self))
