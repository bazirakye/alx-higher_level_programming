#!/usr/bin/python3
"""Reading a file"""


def read_file(filename=""):
    """ function that reads text """
    with open(filename, mode='r', encoding='UTF-8') as myfile:
        print(myfile.read(), end="")
