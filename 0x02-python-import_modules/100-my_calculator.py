#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys
    arguments = sys.argv[1:]
    length = len(arguments)
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(arguments[0])
    b = int(arguments[2])
    if arguments[1] == '+':
        print("{} {} {} = {}".format(a, arguments[1], b, add(a, b)))
    elif arguments[1] == '-':
        print("{} {} {} = {}".format(a, arguments[1], b, sub(a, b)))
    elif arguments[1] == '*':
        print("{} {} {} = {}".format(a, arguments[1], b, mul(a, b)))
    elif arguments[1] == '/':
        print("{} {} {} = {}".format(a, arguments[1], b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
