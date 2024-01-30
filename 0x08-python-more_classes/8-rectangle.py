#!/bin/usr/python3
"""A class representing a rectangle."""

class Rectangle():

    """Attributes:
        width: is The width of the rectangle.
        height: is The height of the rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__ (self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1


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
                rectangle_str += str(self.print_symbol) * self.__width + '\n'
            return rectangle_str.rstrip('\n')

    def __repr__(self):
        """create a string that represent the rectangle 
        for recreating a new instance using eval()."""
        rec = f"Rectangle(width={self.__width}, height={self.__height})"
        return rec

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the rectangle with the larger area.
        """
        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if area_1 >= area_2:
            return rect_1 
        else:
            return rect_2
