#!/usr/bin/python3
"""class Square that inherits Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Rectangle(BaseGeometry):
    """Instantiation with size"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
