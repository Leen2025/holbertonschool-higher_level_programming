#!/usr/bin/python3
"""Defines a subclass MyList that inherits from list.

>>> m = MyList([3, 1, 2])
>>> m.print_sorted()
[1, 2, 3]
>>> print(m)
[3, 1, 2]
"""

class MyList(list):
    """A subclass of list with a method to print sorted elements."""

    def print_sorted(self):
        """Prints the list elements in sorted (ascending) order."""
        print(sorted(self))
