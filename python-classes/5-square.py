#!/usr/bin/python3
"""Module définissant une classe Square avec getter/setter."""


class Square:
    """Représente un carré."""

    def __init__(self, size=0):
        """Initialise le carré.

        Args:
            size (int): taille du carré (0 par défaut).
        """
        self.size = size

    @property
    def size(self):
        """taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """taille avec validation.

        Args:
            value (int): nouvelle taille.

        Raises:
            TypeError: si value n'est pas un entier.
            ValueError: si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """aire du carré."""
        return self.__size ** 2

    def my_print(self):
        """Affiche carré avec des #, vide si 0"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
