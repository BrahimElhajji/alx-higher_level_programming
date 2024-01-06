#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    original_list = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return original_list
    else:
        original_list[idx] = element
        return original_list
