#!/usr/bin/python3
"""class that inherits list
    """


class MyList(list):
    """functtion that prints the list,
    but sorted (ascending sort)"""
    def print_sorted(self):
        print(sorted(self))
