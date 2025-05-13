#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    # key in a_dictionary to check key
    # value in a_dictionary.values() to check value
    # key, value in a_dictionary.items() to check key-value pair
    if value not in a_dictionary.values():
        return a_dictionary
    else:
        for k, v in a_dictionary.copy().items():
            if v == value:
                del a_dictionary[k]
        return a_dictionary


# Another way to delete keys with a specific value
'''
        keys_to_remove = []
        for k, v in a_dictionary.items():
            if v == value:
                keys_to_remove.append(k)

        for k in keys_to_remove:
            del a_dictionary[k]

        return a_dictionary
'''
# Another way to delete keys with a specific value
'''
    for key in a_dictionary:
        if a_dictionary[key] == Value:
            del a_dictionary[key]
'''
