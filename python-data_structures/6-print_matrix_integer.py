#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j in range(len(row)):
            # check if j is the last element of each row
            if j < len(row) - 1:
                print("{:d}".format(row[j]), end=" ")
            else:
                print("{:d}".format(row[j]), end="")
        print()


# Another way to print a matrix
"""
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        return None

    row = 0
    while row < len(matrix):
        i = 0
        while i < len(matrix[0]):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(matrix[row][i]), end="")
            i += 1
        print()
        row += 1
"""
