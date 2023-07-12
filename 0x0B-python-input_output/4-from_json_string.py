#!/usr/bin/python3
"""Defines JSON decoding function."""
import json


def from_json_string(my_str):
    """Return the string representation of a JSON object."""
    return json.loads(my_str)
