#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_s = 0
    total_w = 0
    for i in my_list:
        total_s += (i[0] * i[1])
        total_w += i[1]
    return (total_s / total_w)
