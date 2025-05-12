#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    elif len(tuple_a) > 2:
        tuple_a = (tuple_a[0], tuple_a[1])

    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    elif len(tuple_b) > 2:
        tuple_b = (tuple_b[0], tuple_b[1])

    result = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return result


# Another way to add two tuples - 1
"""
result = []
for i in range(len(tuple_a)):
    result.append(tuple_a[i] + tuple_b[i])
result = tuple(result)
return result
"""
# Another way to add two tuples - 2
""" 
result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
"""
# Another way to add two tuples - 3
"""
result = tuple(map(sum, zip(tuple_a, tuple_b)))
"""
