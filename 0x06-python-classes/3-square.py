#!/usr/bin/python3

"""class for square"""


class Square(object):
    """class that represent a square
    Initialing a instance of the Square class"""
    def __init__(self, size=0):
        """checks if type(size) is an int"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        """checks if size less than 0"""
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        def area(self):
            """Calculate and return the area of the square."""
            return self.__size ** 2
