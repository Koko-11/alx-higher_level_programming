#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print(i)
        break
    print("0{:d}, ".format(i) if i < 10 else "{:d}, ".format(i), end="")
