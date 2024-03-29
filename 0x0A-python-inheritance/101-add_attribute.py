#!/usr/bin/python3
"""Adds a new attribute to an object if it's possible."""


def add_attribute(obj, name, value):
    """checks if it's possible to add a new attribute.
    """
    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__')
       and name in type(obj).__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
