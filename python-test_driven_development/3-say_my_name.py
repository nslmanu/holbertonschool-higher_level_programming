#!/usr/bin/python3
"""affichage nom

say_my_name affiche
"My name is <prénom> <nom>".
"""


def say_my_name(first_name, last_name=""):
    """Affiche My name is <first_name> <last_name>.

    TypeError si l'un des deux n'est pas une string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
