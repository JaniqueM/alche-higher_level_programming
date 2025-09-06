#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    
    Args:
        obj: Any Python object.
    
    Returns:
        list: List of attribute and method names of the object.
    """
    return dir(obj)
