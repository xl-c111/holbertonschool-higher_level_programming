#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    temp = ""
    i = 0
    while i < len(text):
        temp += text[i]
        if text[i] in ".?:":
            print(temp.strip())
            print()
            temp = ""
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    if temp.strip():
        print(temp.strip())
