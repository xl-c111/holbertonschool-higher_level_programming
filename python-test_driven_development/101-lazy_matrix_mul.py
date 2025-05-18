#!/usr/bin/python3
"""
This module provides a function for multiplying two matrices using NumPy.

The function takes two arguments, each expected to be a list of lists
of integers or floats, and returns their matrix product using NumPy's
matrix multiplication function.

All type, shape, and dimension errors are handled by NumPy and will
raise exceptions with standard NumPy error messages.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy's matmul.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        numpy.ndarray: The result of the matrix multiplication.

    Raises:
        TypeError: If the inputs are not valid for matrix multiplication, as
                   determined by NumPy.
        ValueError: If the input shapes are not aligned or contain invalid
                   data, as determined by NumPy.

        All exceptions are raised by NumPy and are not handled
        by this function.
    """

    return np.matmul(m_a, m_b)
