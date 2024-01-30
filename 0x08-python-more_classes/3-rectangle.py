#!/usr/bin/python3
"""Empty class."""


class Rectangle():
    """A class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Attributes:
        width: is The width of the rectangle.
        height: is The height of the rectangle."""

        self.height = height
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

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

    def __str__(self):
        """create a string represent the rectangle
        using the character '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self.__height):
                rectangle_str += '#' * self.__width + '\n'
            return rectangle_str.rstrip()
