#!/usr/bin/python3
def islower(c):
    if 97 <= ord(c) <= 122:
        return True
    else:
        return False

# Another solution
# def islower(c):
#     if 97 <= ord(c) <= 122:
#         return ord('a') <= ord(c) <= ord('z')
