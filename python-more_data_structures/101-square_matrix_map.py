#!/usr/bin/p:ython3

# map(lambda row: ..., matrix): apply a function to each row
# list(map(lambda x: x**2, row)): takes each element x in the row and returns its square (x**2), then wraps the result as a list

def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))


# Another solution by using map and for
"""
return [list(map(lambda x: x ** 2, row)) for row in matrix]
"""

# Another solution by using NumPy
"""
import numpy as np


np_matrix = np.array(matrix)
squared_matrix = np_matrix ** 2
return squared_matrix
"""
