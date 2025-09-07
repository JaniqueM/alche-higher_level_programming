#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from BaseGeometry.

The Rectangle class validates width and height, computes the area, and provides
a string representation of the rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle defined by width and height.

    Attributes:
        __width (int): Private width, validated as a positive integer.
        __height (int): Private height, validated as a positive integer.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with validated dimensions.

        Args:
            width (int): The rectangle width (must be > 0).
            height (int): The rectangle height (must be > 0).
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Format:
            [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
