#!/usr/bin/python3
"""Base geometry module with common interfaces and validators."""


class BaseGeometry:
    """Base class for geometry-related operations and validations."""

    def area(self):
        """Raise an Exception because area is not implemented in the base class."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
            name (str): The name of the variable (for error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
