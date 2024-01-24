#!/usr/bin/python3
"""Creates class Square."""


class Square:
    """class that represent a square
    Initialize an instance of the Square class with
    size and position."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter that returns position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Get area that Returns Area int"""
        return self.__size ** 2

    def my_print(self):
        """Print a square that Returns None"""
        if self.size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for j in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
