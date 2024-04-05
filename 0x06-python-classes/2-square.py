#!/usr/bin/python3
"""3-square.py."""


class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
