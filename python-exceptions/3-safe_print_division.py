#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None
    finally:
        if b != 0:
            print("Inside result: {}".format(result))
        else:
            print("Inside result: None")
