#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide each element of a matrix by a given divisor.

    Parameters:
    - matrix (list of lists): The input matrix to be divided.
    - div (int or float): The divisor for division.

    Returns:
    - list of lists: A new matrix with each
    element rounded to 2 decimal places after division.

    Raises:
    - TypeError:
        - If the matrix is not a list of lists of integers/floats.
        - If the matrix is an empty list.
        - If any row in the matrix is not a list.
        - If any element in the matrix is not an integer or a float.
        - If each row in the matrix does not have the same size.
        - If the divisor is not a number.
    - ZeroDivisionError: If the divisor is 0.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
            "integers/floats")

        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [
            [round(element / div, 2) for element in row] for row in matrix
            ]

    return result_matrix
