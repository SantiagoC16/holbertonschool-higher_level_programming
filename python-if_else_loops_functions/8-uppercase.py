#!/usr/bin/python3
def uppercase(str):
    for s in range(len(str)):
        ordd = ord(str[s])
        if ordd > 64 and ordd < 91:
            print("{}".format(chr(ordd)))
        else:
            strm = ordd - 32
            print("{}".format(chr(strm)))
