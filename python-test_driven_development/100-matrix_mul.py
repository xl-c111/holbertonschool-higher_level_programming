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
                    or if the matrices cannot be multiplied.
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
    # the number of cols in m_a must equal to the number of rows of m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    # i refers to the current row in the result matrix, which corresponds to i-th row in m_a
    for i in range(len(m_a)):
        row = []
        # j refers to the current col in the result matrix, which corresponds to j-th col in m_b
        for j in range(len(m_b[0])):
            total = 0
            # k is summation index, it goes over each each pair of a row and a col, multiplies them one by one
            # and then adds them together
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            row.append(total)
        result.append(row)
    return result


"""
A = [[A11, A12, A13],
     [A21, A22, A23],
     [A31, A32, A33]
]   3 x 3
B = [[B11, B12],
     [B21, B22],
     [B31, B32]
]   3 x 2

the number of cols of A is 3, the number of rows of B is 3, they can be multipled

C = [] is gonna be 3 x 2 matrix
C = [[C11, C12],
     [C21, C22], 
     [C31, C32]
]
C11 = A11 x B11 + A12 x B21 + A13 x B31      
C12 = A11 x B12 + A12 x B22 + A13 x B32      

C21 = A21 x B11 + A22 x B21 + A23 x B31
C22 = A21 x B12 + A22 x B22 + A23 x B32

C31 = A31 x B11 + A32 x B21 + A33 x B31
C32 = A31 x B12 + A32 x B22 + A33 x B32


"""
