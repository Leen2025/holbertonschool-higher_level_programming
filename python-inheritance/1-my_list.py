#!/usr/bin/python3
"""MyList class that inherits from list"""

class MyList(list):
    """
    A custom list class that inherits from Python's built-in list.

    >>> m = MyList([3, 1, 2])
    >>> m.print_sorted()
    [1, 2, 3]
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.

        >>> m = MyList([5, 2, 9])
        >>> m.print_sorted()
        [2, 5, 9]
        """
        print(sorted(self))
