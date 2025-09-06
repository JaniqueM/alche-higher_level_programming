#!/usr/bin/python3
"""Define a class Square based on 3-square.py"""

class Square:
    """Represent a square with size property and area calculation"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size (int): The size of the square (default is 0)
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.size = size  # This will use the setter for validation

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation
        Args:
            value (int): The new size of the square
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
