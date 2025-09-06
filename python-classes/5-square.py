#!/usr/bin/python3
"""Define a class Square based on 4-square.py"""

class Square:
    """Represent a square with size property, area calculation, and print method"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size (int): The size of the square (default is 0)
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.size = size  # Use setter for validation

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

    def my_print(self):
        """Print the square using the '#' character"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
