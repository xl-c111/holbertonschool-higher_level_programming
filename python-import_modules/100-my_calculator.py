#!/usr/bin/python3
import sys
import calculator_1
if __name__ == "__main__":

    arg_count = len(sys.argv) - 1
    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator == "+":
        result = calculator_1.add(a, b)
    elif operator == "-":
        result = calculator_1.sub(a, b)
    elif operator == "*":
        result = calculator_1.mul(a, b)
    elif operator == "/":
        result = calculator_1.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))
