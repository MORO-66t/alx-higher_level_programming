#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square.

    Attributes:
        _size (int): Length of a side of the square.
    """

    def __init__(self, size=0):
        """Initialize the Square instance.

        Args:
            size (int, optional): Length of a side of the square.
            Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Property for the length of a side of this square.

        Returns:
            int: The length of a side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the length of a side of this square.

        Args:
            value (int): The length of a side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of.

        Returns:
            The size.
        """
        return self.__size ** 2

    def my_print(self):
        """Print this."""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
