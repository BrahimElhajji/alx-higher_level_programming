#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    int_numbers = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            int_numbers += 1
        except (TypeError, ValueError):
            continue
    print()
    return int_numbers
