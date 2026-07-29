#!/usr/bin/python3
"""addition d'entiers

add_integer ajoute deux nombres
après validation et format en int.
"""


def add_integer(a, b=98):
    """addition de a et b, bkp en int.
    result TypeError si a ou b n'est ni int ni float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)