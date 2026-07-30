#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """Tests de la fonction max_integer."""

    def test_ordre_list(self):
        """Liste ordre"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_chars(self):
        """Liste strings ordre alpha"""
        self.assertEqual(max_integer(["a", "z", "c"]), "z")
