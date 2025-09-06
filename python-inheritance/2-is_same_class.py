#!/usr/bin/python3
"""
This module provides a function to check if an object is exactly
an instance of a specified class.
"""

def is_same_class(obj, a_class):
    """
    Return True if the object is exactly an instance of the specified class.

    Parameters
    ----------
    obj : any
        The object to check.
    a_class : type
        The class to compare against.

    Returns
    -------
    bool
        True if obj is exactly an instance of a_class, False otherwise.

    Example
    -------
    >>> class MyClass:
    ...     pass
    >>> obj = MyClass()
    >>> is_same_class(obj, MyClass)
    True
    >>> is_same_class(obj, list)
    False
    """
    return type(obj) == a_class
