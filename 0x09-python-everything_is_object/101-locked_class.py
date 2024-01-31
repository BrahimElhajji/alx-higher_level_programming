#!/usr/bin/python3
"""a class with no class or object attribute"""


class LockedClass():
    """calss that prevents the user from dynamically
    creating new instance attributes"""
    __slots__ = ['first_name']

    def __init__(self):
        self.first_name = "first_name"
