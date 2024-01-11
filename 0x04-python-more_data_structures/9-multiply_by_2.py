#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dic = a_dictionary.copy()
    for i in a_dictionary:
        n_dic[i] = n_dic[i] * 2
    return n_dic
