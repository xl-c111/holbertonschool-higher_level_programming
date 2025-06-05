#!/usr/bin/python3
"""This module provides a function to generate Pascal's triangle."""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row (inclusive)"""
    if n <= 0:
        return []
    # initialize the result list res with the first row of pascal's triangle [1]
    res = [[1]]

    # loop to generate the remaining rows
    for i in range(n - 1):

        # pad the last row with a zero at the beginning and end
        temp = [0] + res[-1] + [0]

        # initialize an enpty list to store pascal's triangle's new row
        row = []

        # j is used to loop the temp list
        # len(res[-1])+1 is the length of new row we want to generate, which is always one more than the previous row
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res


# Workflow foe each subsequent row
"""
1, pad the previous row with 0 both at the beginning and end
2, for each position of new row, sum up each pair of adjecent elements in the padded previous row.
"""
