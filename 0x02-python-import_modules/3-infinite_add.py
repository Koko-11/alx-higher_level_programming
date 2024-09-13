#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    length = len(arguments)
    result = 0
    if length == 0:
        print(0)
    else:
        for i in arguments:
            result += int(i)
        print(result)
