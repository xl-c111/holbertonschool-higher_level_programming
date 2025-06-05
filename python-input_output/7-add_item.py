#!/usr/bin/python3
"""This script adds all command-line arguments to a list and saves them in a
JSON file. If the file exists, previous data will be loaded and extended with
the new arguments; otherwise, a new file will be created."""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# check if add_item.json exists.
# use load_from_ json_file to read existing content, if the file is missing, start with an empty list
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# retrieve the command line using (sys.argv[1:]) and extend the list with them
my_list.extend(sys.argv[1:])
# use save_to_json_file to save the final list back to add_item.json
save_to_json_file(my_list, filename)


# difference between extend() and append()
"""
- extend() will add each element from the iterable(e.g. list) as a separate item in the list
my_list = [1, 2, 3]
my_list.extend([4, 5])
result: [1, 2, 3, 4, 5]

append() will add the entire argument as a single element(no matter it's a list, string...)
my_list = [1, 2, 3]
my_list.append([4, 5])
result: [1, 2, 3, [4, 5]]
"""

# why sys.argv[1:]
"""
sys.argv is a list that contains all the command-line arguments passed to the script.
the first argument sys.argv[0] is always the name of the script.
sys.argv[1:] skips the script name and gets only user's input.
"""
