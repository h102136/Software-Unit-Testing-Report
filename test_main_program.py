import unittest
from guess_game import main

def test_main(self):
    with unittest.mock.patch("builtins.input", side_effect=["1234", "q"]):
        with unittest.mock.patch("builtins.print"):
            main()  # Test the main loop
    # Add more tests to cover different scenarios in the main loop