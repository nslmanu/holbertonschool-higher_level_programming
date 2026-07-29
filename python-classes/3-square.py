#!/usr/bin/python3
"""Module définissant une classe Square avec taille validée."""


class Square:
    """Représente un carré."""

    def __init__(self, size=0):
        """Initialise le carré.

        Args:
            size (int): taille du carré (0 par défaut).

        Raises:
            TypeError: si size n'est pas un entier.
            ValueError: si size est négatif.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Aire du carré."""
        return self.__size ** 2
