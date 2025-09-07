#!/usr/bin/python3
"""Base geometry module with common interfaces and validators."""


class BaseGeometry:
    """Base class for geometry-related operations and validations."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that 'value' is an integer greater than 0.

        Args:
            name (str): Variable name used in error messages.
            value (int): Value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
