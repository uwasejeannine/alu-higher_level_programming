#!/usr/bin/python3
"""This module provides tools for working with squares."""

class Square:
    """A square with a side length.

    Attributes:
        size (int): The length of each side of the square.
    """

    def __init__(self, size=0):
        """Creates a new Square with a given side length.

        Args:
            size (int): The length of each side of the square.
        """
        self.size = size

    def area(self):
        """Returns the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.size ** 2
