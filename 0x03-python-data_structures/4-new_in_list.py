#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return
   new = my_list.copy()
   if 0 <= idx < len(new):
       new[idx] = element
       return new
