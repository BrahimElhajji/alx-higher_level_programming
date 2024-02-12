#!/usr/bin/python3
"""Class Rctangle Module that inherits Base Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def integer_validator(self, name, value):
        """a validation function for height and width"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def validate_position(self, name, value):
        """a validation function for x and y"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """function that initialize instances"""
        super().__init__(id)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.validate_position("x", x)
        self.validate_position("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute."""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute."""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x attribute."""
        self.validate_position("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y attribute."""
        self.validate_position("y", value)
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """that prints in stdout of the Rectangle instance
        with the character #"""
        for j in range(self.y):
            print()

        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

        def update(self, *args, **kwargs):
            """function that assigns an argument to each attribute"""
        if args is not None and len(args) is not 0:
            list_args = ['id', 'width', 'height', 'x', 'y']
            for arg in range(len(args)):
                setattr(self, list_args[arg], args[arg])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """function that returns the dictionary
        representation of a Rectangle"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
