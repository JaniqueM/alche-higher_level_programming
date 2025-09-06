"""
lookup.py

This module provides a function to retrieve all available attributes
and methods of a given Python object.

Functions:
----------
lookup(obj)
    Returns a list of the names of attributes and methods of the object.
"""

def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Parameters
    ----------
    obj : any
        The object whose attributes and methods are to be retrieved.

    Returns
    -------
    list
        A list containing the names of the object's attributes and methods.

    Example
    -------
    >>> class Test:
    ...     def method(self):
    ...         pass
    >>> t = Test()
    >>> lookup(t)
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', ..., 'method']
    """
    return dir(obj)
