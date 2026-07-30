#!/usr/bin/python3
"""affichage de carré.

Fournit print_square qui affiche un carré
de taille size avec le caractère #.
"""


def print_square(size):
    """dessine un carré de # de côté size.

    check TypeError si size n'est pas un int,
    ValueError si size est négatif.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
