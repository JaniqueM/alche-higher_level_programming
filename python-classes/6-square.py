#!/usr/bin/python3
"""
5-square.py

This module defines a class Square that represents a square with size and
position. It includes size and position validation, area calculation, and
a method to print the square using the '#' character with position offsets.
"""


class Square:
    """Represent a square with size, position, and print capability."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The pos
