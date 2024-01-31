#!/usr/bin/python3
"""
    function that dds two numbers and returns their sum.
    - a (int or float): The first number.
    - b (int or float, optional): The second number. Default is 98.
    """


def add_integer(a, b=98):
    """ Raises:
    - TypeError: If either 'a' is not an integer or float.
    - TypeError: or 'b' is not an integer or float."""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
