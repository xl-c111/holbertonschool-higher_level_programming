#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            # increase count only when my_list[i] printed successfully as an int
            count += 1
        except (TypeError, ValueError):
            pass
        # increase i whether the current element is int or not
        # -> ensure access first x element, print only integers
        i += 1
    print()
    return count


# Another solution - Using for loop
'''
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
'''
