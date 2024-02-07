#!/usr/bin/python3
"""adds all arguments to a Python list,
and then save them to a file"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    item_L = load_from_json_file("add_item.json")
except FileNotFoundError:
    item_L = []

if __name__ == "__main__":
    item_L.extend(sys.argv[1:])
    save_to_json_file(item_L, "add_item.json")
