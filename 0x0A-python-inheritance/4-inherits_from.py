#!/usr/bin/python3
"""function that returns True if the object is an instance
of a class that inherited from the specified class
    """


def inherits_from(obj, a_class):
    """checks if the child class"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
