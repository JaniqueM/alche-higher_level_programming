#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance
of a specified class or an instance of a subclass thereof.
"""

def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of a_class or an instance
    of a class that inherited from a_class; otherwise False.

    Parameters
    ----------
    obj : any
        The object to check.
    a_class : type
        The class to compare against.

    Returns
    -------
    bool
        True if obj is an instance of a_class or its subclass, False otherwise.

    Example
    -------
    >>> class Base:
    ...     pass
    >>> class Derived(Base):
    ...     pass
    >>> obj1 = Base()
    >>> obj2 = Derived()
    >>> is_kind_of_class(obj1, Base)
    True
    >>> is_kind_of_class(obj2, Base)
    True
    >>> is_kind_of_class(obj2, list)
    False
    """
    return isinstance(obj, a_class)
