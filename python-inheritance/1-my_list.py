#!/usr/bin/python3
"""Defines a subclass MyList that inherits from list."""

class MyList(list):
    """A subclass of list with a method to print sorted elements."""

    def print_sorted(self):
        """Prints the list elements in sorted (ascending) order."""
        print(sorted(self))
