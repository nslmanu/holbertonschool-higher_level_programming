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

    def test_float_max(self):
        """Liste max float"""
        self.assertEqual(max_integer([0.1, 0.4, 0.3]), 0.4)

    def test_first_max(self):
        """Liste max first"""
        self.assertEqual(max_integer([1, 0.1, 0.4, 0.3]), 1)

    def test_empty_list(self):
        """Liste vide None."""
        self.assertIsNone(max_integer([]))
