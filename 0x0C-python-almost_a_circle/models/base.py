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
        if list_objs is not None:
            for o in list_objs:
                list_objs = [o.to_dictionary()]
        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string(list_objs))

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
            dummy_instance = cls(10, 10)
        elif cls.__name__ == "Square":
            dummy_instance = cls(10)
        else:
            dummy_instance = None
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Function that returns a list of instances."""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as f:
                j_str = f.read()
                return [cls.create(**d) for d in cls.from_json_string(j_str)]
        except FileNotFoundError:
            return []
