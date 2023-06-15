#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    only_set_1 = set_1 - set_1.intersection(set_2)
    only_set_2 = set_2 - set_2.intersection(set_1)

    joined = only_set_2 | only_set_1
    return (joined)
