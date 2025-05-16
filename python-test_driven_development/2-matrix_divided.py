#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.

The function `matrix_divided` takes a matrix (a list of lists of integers
or floats) and a divisor, and returns a new matrix with all elements divided
by the divisor, rounded to two decimal places.

It checks whether the type of matrix, rows and elements inside of each row
is integer or float.
It checks if each row of matrix has the same length.
It validates if the divisor is a non-zero number.

Raises:
    TypeError: If the matrix is not a list of lists of integers/floats,
               if the rows are not of the same size,
               or if the divisor is not a number.
    ZeroDivisionError: If the divisor is zero.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number and return a new matrix.

    Args:
        matrix: a matrix represented as a list of lists, where each inner
            list contains integers or floats, and all rows are of equal size.
        div: the number to divide each elements of the matrix.

    Return:
        a list of list of float: a new matrix with each element divided by
        'div', rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   if the rows are not of the same size,
                   or if the divisor is not a number.
        ZeroDivisionError: If div is zero.
    """

    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats"
                )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix
