#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    i = 0
    while i < x:
        try:
            # print the element at index i, if i within x, succeeds.
            # if i out of bound, this line will raise IndexError
            print("{}".format(my_list[i]), end="")
            # increase the count only when my_list[i] is actually printed
            count += 1
            # only move to next element when my_list[i] is accessed successfully
            # -> ensure to print up to x element, stop on IndexError
            i += 1
        except IndexError:
            break
    print()
    return count


# Another solution - Using for loop
'''
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]))
            count += 1
        except IndexError:
            break
    print()
    return count
'''
