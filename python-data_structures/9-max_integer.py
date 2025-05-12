#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        largest = my_list[0]

        for val in my_list:
            if val > largest:
                largest = val
        return largest
