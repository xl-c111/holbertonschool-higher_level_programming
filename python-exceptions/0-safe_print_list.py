#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    i = 0
    while i < x:
        try:
            # attempt to print the element at index i, if i within x, succeeds. If i out of bound, this line will raise IndexError
            print("{}".format(my_list[i]), end="")
            # this line increases the count only when my_list[i] is actually printed
            count += 1
            # only move to next element when my_list[i] is accessed successfully
            i += 1
        except IndexError:
            break
    print()
    return count
