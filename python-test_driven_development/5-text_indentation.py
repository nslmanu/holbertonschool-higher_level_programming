#!/usr/bin/python3
"""indentation de texte.

text_indentation qui affiche un texte avec
2 sauts de ligne après chaque '.', '?' et ':'.
"""


def text_indentation(text):
    """Affiche text avec 2 nouvelles lignes après ., ? et :.

    Lève TypeError si text n'est pas une string.
    """

    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            i += 1
