#!/usr/bin/python3
"""Matrix à diviser.

div must be a number (integer or float), otherwise
raise a TypeError exception with the message
div must be a number
div can't be equal to 0, otherwise raise
a ZeroDivisionError exception with the
message division by zero
"""


def matrix_divided(matrix, div):
    """div must be a number (integer or float),
    otherwise raise a TypeError exception with
    the message div must be a number

    div can't be equal to 0, otherwise
    raise a ZeroDivisionError
    exception with the message division by zero
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(n, (int, float))
                    for row in matrix for n in row)):
        raise TypeError(err)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
