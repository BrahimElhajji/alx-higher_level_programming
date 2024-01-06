#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    or_list = my_list
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        or_list.remove(my_list[idx])
        return or_list
