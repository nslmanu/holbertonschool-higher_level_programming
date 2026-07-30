#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests de la fonction max_integer."""

    def test_ordered_list(self):
        """Liste ordonnée."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

