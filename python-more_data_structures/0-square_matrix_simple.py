#!/usr/bin/python3
def square_matrix_simple(matrix=[]):


new_matrix = []
for row in matrix:
    new_row = []
    for element in row:
        new_row.append(element ** 2)
    new_matrix.append(new_row)
return new_matrix


# Another way to compute the square value of all integers of a matrix

# for row in matrix: outer list comprehension -> iterate over each row
# for element in row: inner list comprehensionz -> iterate over each element in the current row
# combined logic: outer loop builds new row, inner loop squares each element in that row

"""
    new_matrix = [[element**2 for element in row] for row in matrix]
    return new_matrix
"""
