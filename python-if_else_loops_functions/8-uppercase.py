#!/usr/bin/python3
def uppercase():
    for s in range(len(str)):
        ordd = ord(str[s])
        if ordd > 96 and ordd < 123:
            strm = ordd - 32
        print("{}".format(chr(strm)), end="")
print()
