#!/usr/bin/python3
"""
Defines matrix_divided function
This function divides all elements of a matrix
After computation it returns a new matrix
"""


def matrix_divided(matrix, div):
    """ Function for dividing all elements of a matrix
    Args:
        matrix (list): list of lists of integers or floats.
        div (int) or (float): divisor of the elements.
    """
    if isinstance(matrix, list):
        for i in range(0, len(matrix)):
            if isinstance(matrix[i], list):
                a = len(matrix[i])
                break
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError("matrix must \
be a matrix (list of lists) of integers/floats")
            for num in row:
                if not isinstance(num, int):
                    if not isinstance(num, float):
                        raise TypeError("matrix \
must be a matrix (list of lists) of integers/floats")
            if len(row) != a:
                raise TypeError("Each row of the \
matrix must have the same size")
    if not isinstance(div, int):
        if not isinstance(div, float):
            raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        tmp = []
        for i in range(0, len(row)):
            result = row[i] / div
            result = round(result, 2)
            tmp.append(result)
        new_matrix.append(tmp)
    return new_matrix
