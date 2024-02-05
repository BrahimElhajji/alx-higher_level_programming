#!/usr/bin/python3
"""function that returns the list of
    available attributes and methods of an object"""


def lookup(obj):
    """Returns:
    - List of strings: Names of attributes
    and methods of the object"""

    return(dir(obj))
