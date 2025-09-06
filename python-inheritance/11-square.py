#!/usr/bin/python3
"""
Square module
Defines a Square class that inherits from Rectangle (9-rectangle.py)
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    
    Attributes:
        __size (int): The size of the square sides (private)
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square's sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is <= 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The format is [Square] <width>/<height>
        """
        return f"[Square] {self.__size}/{self.__size}"
