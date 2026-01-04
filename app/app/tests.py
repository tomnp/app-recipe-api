"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Tests for calc module."""

    def test_add_numbers(self):
        """Test adding two numbers to gethers."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Test subtracting two numbers to gethers."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
