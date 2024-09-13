#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    p = len(argv) - 1
    if p < 1:
        print("{} arguments.".format(p))
    elif p == 1:
        print("{} arguments.".format(p))
    else:
        print("{} arguments.".format(p))
    for i in range (p):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
