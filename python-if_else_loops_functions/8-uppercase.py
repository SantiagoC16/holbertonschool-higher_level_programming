#!/usr/bin/python3
def uppercase(str):
    strm = 0
    for s in range(len(str)):
        ordd = ord(str[s])
        if ordd > 96 and ordd < 123:
            strm = ordd - 32
        print("{}".format(chr(strm)), end="")
print()
