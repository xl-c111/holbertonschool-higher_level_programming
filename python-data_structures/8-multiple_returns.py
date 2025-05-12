#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        return (0, None)
    else:
        return (len(sentence), sentence[0])


# Another way to check if str is empty
"""
if len(str) == 0:
"""
