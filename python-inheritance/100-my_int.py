#!/usr/bin/python3
"""Defines a rebel integer class MyInt."""


class MyInt(int):
    """A class that inverts == and != operators."""

    def __eq__(self, other):
        """Invert the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the != operator."""
        return super().__eq__(other)
