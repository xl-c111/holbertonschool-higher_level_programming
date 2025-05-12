#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in set(my_list):
        sum += i
    return sum


# Another way to get a uniq list - 1
'''
def uniq_add(my_list=[]):
    uniq_list = []
    for item in my_list:
        if item not in uniq_list:
            uniq_list.append(item)
'''

# Another way to get a uniq list - 1
'''
from collections import OrderedDict


def uniq_add(my_list=[]):
    uniq_list = list(OrderedDict.fromkeys(my_list))
    sum = 0
    for i in uniq_list:
        sum += i
    return sum
'''
