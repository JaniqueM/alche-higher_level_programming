#!/usr/bin/python3
"""Module defining a Rectangle class that inherits from BaseGeometry"""

from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle with width and height"""

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width (int): Width of the rectangle (private, validated)
            height (int): Height of the rectangle (private, validated)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
