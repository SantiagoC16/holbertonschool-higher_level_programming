#!/usr/bin/python3
def uppercase(str):
    if ord(str) > 64 and ord(str) < 91:
        strm = ord(str) + 42
        strmm = chr(strm)
        print (strmm)
    else:
        print (str)
