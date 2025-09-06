#!/usr/bin/python3
"""Define a class Square based on 5-square.py"""

class Square:
    """Represent a square with size, position, area calculation, and print method"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square
        Args:
            size (int): The size of the square (default is 0)
            position (tuple): The position of the square (default is (0, 0))
        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers
            ValueError: If size is less than 0
        """
        self.size = size  # validated by setter
        self.position = position  # validated by setter

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character with position offset"""
        if self.__size == 0:
            print()
            return

        # print vertical offset
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            # print horizontal offset
            print(" " * self.__position[0] + "#" * self.__size)
