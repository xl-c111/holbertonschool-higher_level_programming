#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    temp = ""
    for char in text:
        temp += char
        if char in ".?:":
            print(temp.strip())
            print()
            temp = ""
    if temp.strip():
        print(temp.strip())

    # i = 0
    # temp = ""
    # while i < len(text):
    #     temp += text[i]
    #     if text[i] == '.' or text[i] == '?' or text[i] == ':':
    #         print(temp.strip())
    #         print()
    #         temp = ""
    #         i += 1
    #         while i < len(text) and text[i] == " ":
    #             i += 1
    #         continue
    #     i += 1
    # if temp.strip():
    #     print(temp.strip())
