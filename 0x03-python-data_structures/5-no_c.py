#!/usr/bin/python3
def no_c(my_string):

    without_c = ""
    c_string = my_string
    for c in c_string:
        if c.lower() != 'c':
            without_c += c 
    return without_c
