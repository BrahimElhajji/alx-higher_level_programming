#!/usr/bin/python3
"""class BaseGeometry (based on 6-base_geometry.py)
    """


class BaseGeometry:
    """BaswGeometry class"""
    def area(self):
        """def area(self):
    that raises an Exception with the message area()"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """def integer_validator(self, name, value):
    that validates value"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
