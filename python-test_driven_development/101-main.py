#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
# print(lazy_matrix_mul([[1, "a"], [3, 4]], [[1, 2], [3, 4]]))
# print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], ["b", 4]]))
# print(lazy_matrix_mul("Holberton", [[1, 2], [3, 4]]))
# print(lazy_matrix_mul([[1, 2, 3]], [[4, 5], [6, 7]]))
# print(lazy_matrix_mul([1, 2], [[5, 6], [7, 8]]))
# print(lazy_matrix_mul([[5, "6"], [7, 8]], [[5, 6], [7, 8]]))
# print(lazy_matrix_mul([[]], [[5, 6], [7, 8]]))
