#!/usr/bin/python3
""" Function that defines an object(obj) attribute lookup"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
