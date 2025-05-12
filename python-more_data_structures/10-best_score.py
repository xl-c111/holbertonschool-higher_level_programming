#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        max_key = max(a_dictionary, key=a_dictionary.get)
        return max_key


# Another way to get max value - 1
'''
max_val = max(a_dictionary.values())
    for key in a_dictionary:
        if a_dictionary[key] == max_val: 
            return key
'''
# Another way to get max value - 2
'''
 max_key = max(a_dictionary, key=lambda key: a_dictionary[key])
'''
