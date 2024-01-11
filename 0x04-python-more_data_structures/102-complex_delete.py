#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    for k in a_dictionary.items():
        if k == value:
            del a_dictionary[k]
    return a_dictionary
