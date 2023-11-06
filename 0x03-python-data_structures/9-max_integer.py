#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None

    copied = my_list.copy()
    copied.sort()
    return copied[-1]
