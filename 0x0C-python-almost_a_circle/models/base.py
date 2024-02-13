#!/usr/bin/python3
"""Class Base Module"""
import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instances initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function that list to json string"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """function that save objects to file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            for obj in list_objs:
                json_string = cls.to_json_string([obj.to_dictionary()])
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """function  that that returns the list
        of the JSON string representation"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Function that returns an instance
        with all attributes set from the provided dictionary"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(5, 5)
        elif cls.__name__ == "Square":
            dummy_instance = cls(5)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """function  that returns a list of instances"""

        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as f:
                json_string = f.read()
        except FileNotFoundError:
            return []

        dictionaries = cls.from_json_string(json_string)
        instances = [cls.create(**dictionary) for dictionary in dictionaries]
        return instances
