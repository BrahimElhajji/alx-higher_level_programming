#!/usr/bin/python3

"""class for square"""


class Square(object):
    """class that represent a square
    Initialing a instance of the Square class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Getter to retrieve the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set the size attribute with type
            and value validation"""
        """Check if value is an integer"""
        if type(value) != int:
            raise TypeError("size must be an integer")
            """Check if value is less than 0"""
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
