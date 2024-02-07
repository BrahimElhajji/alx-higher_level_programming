#!/usr/bin/python3
"""Student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """function that Instantiat with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function that retrieves a dictionary representation
        of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}

    def reload_from_json(self, json_data):
        """function that replaces all attributes of the Student instance"""
        for key, value in json_data.items():
            setattr(self, key, value)
