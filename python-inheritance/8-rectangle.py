#!/usr/bin/python3
"""Module defining a Rectangle class that inherits from BaseGeometry

This module contains a Rectangle class that represents a rectangle
with width and height. Both dimensions are private and validated
using the BaseGeometry's integer_validator method.
"""

from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle shape with validated width and height.

    Inherits from BaseGeometry. The width and height must be positive
    integers and are stored as private attributes.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle (must be positive integer).
            height (int): Height of the rectangle (must be positive integer).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height <= 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
