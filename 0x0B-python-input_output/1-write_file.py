#!/usr/bin/python3
"""Whriting to a file"""


def write_file(filename="", text=""):
    """This function writes to a string and retuns lenth of characters written"""
    with open(filename, mode='w', encoding='utf-8') as myfile:
       return myfile.write(text)
