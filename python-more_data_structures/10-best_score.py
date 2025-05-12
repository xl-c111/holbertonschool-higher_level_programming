#!/usr/bin/python3
from curses import keyname


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        max_val = max(a_dictionary.values())
        max_keys = []
        for key in a_dictionary:
            if a_dictionary[key] == max_val:
                max_keys.append(key)
        return max_keys
