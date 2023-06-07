#!/usr/bin/python3

def uppercase(str):
    upper_string = ""
    for char in str:
        lower_ascii = ord(char)
        upper_ascii = lower_ascii - 32
        upper = chr(upper_ascii)
        upper_string += upper
    print(upper_string)
