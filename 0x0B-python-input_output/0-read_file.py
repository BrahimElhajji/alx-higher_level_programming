#!/usr/bin/python3
"""function that reads the file"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it """
    with open(filename, 'r', encoding="utf-8") as f:
        file_cont = f.read()
        print(file_cont, end="")
