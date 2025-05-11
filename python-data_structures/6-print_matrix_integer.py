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
