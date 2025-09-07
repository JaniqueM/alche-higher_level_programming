#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class provides a foundation for geometry-related operations.
    """

    def area(self):
        """
        Raises an Exception since area is not implemented.
        This method should be overridden by subclasses.
        """
        raise Exception("area() is not implemented")
