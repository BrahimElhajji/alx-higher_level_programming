#!/usr/bin/python3
"""Empty class"""


class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Attributes:
        width: is The width of the rectangle.
        height: is The height of the rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
