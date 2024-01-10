#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    n_matrix = []
    for row in matrix:
        squared_row = []
        for n in row:
            squared_row.append(n ** 2)
        n_matrix.append(squared_row)

    return n_matrix
