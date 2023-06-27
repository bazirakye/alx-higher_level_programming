#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a/b
        print("Inside result: {}".format(div), end='')
    except ZeroDivisionError:
        div = None
        print("Inside result: {}".format(div), end='')
    finally:
        return div
