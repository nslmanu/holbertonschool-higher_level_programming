#!/usr/bin/python3
"""Module définissant une classe Square avec taille et position."""


class Square:
    """Représente un carré."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise le carré.

        Args:
            size (int): taille du carré (0 par défaut).
            position (tuple): décalage horizontal et vertical.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Récupère la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille avec validation.

        Raises:
            TypeError: si value n'est pas un entier.
            ValueError: si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


