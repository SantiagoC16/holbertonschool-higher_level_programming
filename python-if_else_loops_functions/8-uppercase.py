#!/usr/bin/python3
def uppercase():
    for s in range(len(str)):
        ordd = ord(str[s])
        if ordd > 64 and ordd < 91:
            print("{}".format(chr(ordd)), end="")
        else:
            strm = ordd - 32
            print("{}".format(chr(strm)), end="")
print()
