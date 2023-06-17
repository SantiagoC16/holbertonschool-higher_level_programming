#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        TypeError("text must be a string")
    flag = False
    for t in text:
        if t == "." or t == ":" or t == "?":
            print(t)
            print()
            flag = True
        elif t != ' ' or not flag:
            print(t, end="")
            flag = False
