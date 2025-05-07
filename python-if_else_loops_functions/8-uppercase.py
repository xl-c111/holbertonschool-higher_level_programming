#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            uppercase_str += chr(ord(i) - 32)
        else:
            uppercase_str += i
    print(uppercase_str)
