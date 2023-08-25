import unittest
from guess_game import compare_numbers

def test_compare_numbers(self):
    self.assertEqual(compare_numbers("1234", "5678"), (0, 0))
    self.assertEqual(compare_numbers("1234", "1234"), (4, 0))
    self.assertEqual(compare_numbers("1234", "4321"), (0, 4))
    self.assertEqual(compare_numbers("1234", "1243"), (2, 2))
    self.assertEqual(compare_numbers("1122", "2211"), (0, 4))  # Test repeated digits
    self.assertEqual(compare_numbers("1234", "5671"), (0, 1))  # Test partial match

