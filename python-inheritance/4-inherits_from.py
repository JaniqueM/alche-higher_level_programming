#!/usr/bin/python3
"""
inherits_from.py

This module provides a function to check whether an object is an instance
of a class that inherited (directly or indirectly) from a specified class.
"""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherits from a_class.

    Parameters
    ----------
    obj : any
        The object to check.
    a_class : type
        The class to compare against.

    Returns
    -------
    bool
        True if obj is an instance of a subclass of a_class (but not a_class itself),
        False otherwise.

    Example
    -------
    >>> class Base:
    ...     pass
    >>> class Derived(Base):
    ...     pass
    >>> class MoreDerived(Derived):
    ...     pass
    >>> b = Base()
    >>> d = Derived()
    >>> m = MoreDerived()
    >>> inherits_from(b, Base)
    False
    >>> inherits_from(d, Base)
    True
    >>> inherits_from(m, Base)
    True
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
