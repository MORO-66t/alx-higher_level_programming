#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square.

    Attributes:
        _size (int): Length of a side of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square instance.

        Args:
            size (int, optional): Length of a side of the square.
            Defaults to 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property for the length of a side of this square.

        Returns:
            int: The length of a side of the square.
        """
        return (self.__size)

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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property for the length of a side of this square.

        Returns:
            int: The length of a side of the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter for the length of a side of this square.

        Args:
            value (int): The length of a side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of.

        Returns:
            The size.
        """
        return self.__size ** 2

    def my_print(self):
        """Print this."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
