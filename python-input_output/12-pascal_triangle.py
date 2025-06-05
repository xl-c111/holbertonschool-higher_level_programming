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


# Another Solution
def pascal_triangle(n):
    if n <= 0:
        return []

    # initialize a main list triangle to store all rows
    triangle = []

    # loop through 0 to n-1 to build each row
    for i in range(n):

        # each rtow starts with 1
        new_row = [1]

        # j is used to loop through the middle position, its value = sum of two elemnts above it
        for j in range(1, i):
            new_row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # except the first row, each row ends with 1
        if i > 0:
            new_row.append(1)
        triangle.append(new_row)
    return triangle


# workflow
"""
1, i is used to loop through each row 
2, each row  starts with 1, new_row = [1]
3, j is used to loop through the middle position (except beginning and end position) 
4, each element in the middle position of row == triangle[i -1][j - 1] + triangle[i - 1][j]
5, if i > 0 (skips the first row), each row ends with 1
"""
