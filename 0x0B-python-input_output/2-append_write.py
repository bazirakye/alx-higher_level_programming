#!/usr/bin/python3
""" appending text"""


def append_write(filename="", text=""):
    """Appending text to file"""
    with open(filename, mode='a', encoding='utf-8') as myfile:
        return myfile.write(text)
