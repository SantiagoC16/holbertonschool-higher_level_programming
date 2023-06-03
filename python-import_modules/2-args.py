#!/usr/bin/env python3
if __name__ == "__main__":
    import sys
    arguments = len(sys.argv) - 1
    if arguments == 0:
        print("{} arguments.".format(arguments))
    elif arguments == 1:
        print("{} argument:".format(arguments))
    else:
        print("{} arguments:".format(arguments))
    for argc in range(1, arguments + 1):
        print("{}: {}".format(argc, sys.argv[argc]))
