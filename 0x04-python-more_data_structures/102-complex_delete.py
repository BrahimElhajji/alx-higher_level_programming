#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    d_keys = []

    for k, v in a_dictionary.items():
        if v == value:
            d_keys.append(k)

    for k in d_keys:
        del a_dictionary[k]

    return a_dictionary
