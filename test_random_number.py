import unittest
from guess_game import generate_random_number


def test_generate_random_number(self):
    random_number = generate_random_number()
    self.assertTrue(1000 <= random_number <= 9999)



if __name__ == "__main__":
    unittest.main()
