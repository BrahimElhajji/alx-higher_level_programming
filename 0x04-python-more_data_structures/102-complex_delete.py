#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    for k in a_dictionary.keys():
        if k == value:
            del a_dictionary
    return a_dictionary
