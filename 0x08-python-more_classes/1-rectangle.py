#!/bin/usr/python3
"""A class representing a rectangle."""

class Rectangle():

    """Attributes:
        width: is The width of the rectangle.
        height: is The height of the rectangle."""

    def __init__ (self, width=0, height=0):
        self.height = height
        self.width = width

    @property    
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter method for the height attribute."""
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("idth must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter method for the height attribute."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("idth must be >= 0")
        else:
            self.__width = width
