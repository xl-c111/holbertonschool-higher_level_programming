#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    arg_count = len(sys.argv) - 1
    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = sys.argv[2]
    if operator not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if operator == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif operator == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif operator == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif operator == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
