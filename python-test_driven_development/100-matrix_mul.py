#!/usr/bin/python3
"""
This module provides a function to multiply two matrices.

It checks type and value of two matrixes to ensure that the inputs are proper
matrices.
It raises informative errors when the inputs do not meet these requirements.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result as a new matrix.

    Args:
        m_a (list of lists of int/float): The first matrix to multiply.
        m_b (list of lists of int/float): The second matrix to multiply.

    Returns:
        list of lists of int/float: The product matrix.

    Raises:
        TypeError: If either m_a or m_b is not a list, not a list of lists,
                   not a rectangle.
                   or contains elements that are not integers or floats,
        ValueError: If either m_a or m_b is empty or contains empty rows,
                    or if the matrices cannot be multiplied due to shape
                    incompatibility.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            row.append(total)
        result.append(row)
    return result
