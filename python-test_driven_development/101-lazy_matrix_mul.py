#!/usr/bin/python3
"""
This module provides a function for multiplying two matrices using NumPy.

It validates that both matrices are proper lists of lists containing only
integers or floats, with consistent row sizes, and compatible dimensions
for multiplication. 
It returns a NumPy array.

Raises:
    TypeError: If the input matrices are not lists of lists of numbers,
               or have inconsistent row sizes.
    ValueError: If either matrix is empty, or if the matrices cannot be
               multiplied due to dimension mismatch.
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy after validating input types and
    shapes.

    Args:
        m_a (list of lists of int/float): The first matrix to multiply.
        m_b (list of lists of int/float): The second matrix to multiply.

    Returns:
        The resulting product matrix.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers/floats,
            or if their rows are not all the same size.
        ValueError: If m_a or m_b is empty, or if the matrices cannot
                    be multiplied.
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

    a = np.array(m_a)
    b = np.array(m_b)
    c = a.dot(b)
    return c
