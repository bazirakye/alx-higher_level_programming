#!/usr/bin/python3

def add_integer(a, b=98):
    """ functions thata adds 2 integers
        Args:
        a - first interger
        b - second integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (a + b)
