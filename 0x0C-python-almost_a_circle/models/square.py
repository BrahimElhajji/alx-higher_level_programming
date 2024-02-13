#!/usr/bin/python3
"""Class Square Module that inherits Rectangle Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """function that initialize instances"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """Getter method for size attribute."""
        return self.height

    @size.setter
    def size(self, value):
        """Setter method for y attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """function that assigns an argument to each attribute"""
        if args:
            list_args = ['id', 'size', 'x', 'y']
            for arg in range(len(args)):
                setattr(self, list_args[arg], args[arg])
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """that returns the dictionary representation of a Square"""
        return {'id': self.id, 'x': self.x,
                'size': self.width, 'y': self.y}
