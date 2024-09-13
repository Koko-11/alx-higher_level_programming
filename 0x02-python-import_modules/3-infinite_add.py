#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name
    total = 0

    for arg in argv:
        total += int(arg)

    print(total)
