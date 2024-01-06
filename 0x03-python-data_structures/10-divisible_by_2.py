#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    o_list = []
    for i in my_list:
        if i % 2 == 0:
            o_list.append(True)
        elif i % 2 == 1:
            o_list.append(False)
    return o_list
