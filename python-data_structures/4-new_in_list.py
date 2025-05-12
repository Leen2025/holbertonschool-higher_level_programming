#!/usr/bin/python3
# 4-new_in_list.py
# Leen Alsaleh <10693@holbertonschool.com>

def new_in_list(my_list, idx, element):
    # Return a copy if index is invalid (negative or out of range)
    if idx < 0 or idx >= len(my_list):
        return my_list[:]

    # Create a shallow copy of the original list
    copy = [x for x in my_list]
    copy[idx] = element  # Replace the element at the given index
    return copy
