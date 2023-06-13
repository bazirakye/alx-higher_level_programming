#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list or len(my_list) == 0:
        return
    sort_list = sorted(my_list)
    return sort_list[-1]
