#!/usr/bin/python3
"""adds all arguments to a Python list,
and then save them to a file"""
import sys
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file"""

    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)


try:
    item_L = load_from_json_file("add_item.json")
except FileNotFoundError:
    item_L = []

item_L.extend(sys.argv[1:])
save_to_json_file(item_L, "add_item.json")
