#!/usr/bin/python3
"""Create a function that returns a list of lists of integers"""


def pascal_triangle(n):
    """ that returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    pascal = [[1]]
    for i in range(1, n):
        old_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(old_row[j - 1] + old_row[j])
        new_row.append(1)
        pascal.append(new_row)

    return pascal
