import unittest
from guess_game import get_user_guess

def test_get_user_guess(self):
    with unittest.mock.patch("builtins.input", side_effect=["12345", "abcd", "123", "q"]):
        self.assertEqual(get_user_guess(), None)  # Test user quitting
        self.assertEqual(get_user_guess(), None)  # Test invalid input (not a digit)
        self.assertEqual(get_user_guess(), None)  # Test invalid input (not 4 digits)
        self.assertEqual(get_user_guess(), "1234")  # Test valid input
