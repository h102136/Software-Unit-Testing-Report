import unittest
from guess_game import generate_random_number, compare_numbers

class TestGame(unittest.TestCase):
    def test_generate_random_number(self):
        random_number = generate_random_number()
        self.assertTrue(1000 <= random_number <= 9999)

    def test_compare_numbers(self):
        secret_number = "1234"
        self.assertEqual(compare_numbers(secret_number, "5678"), (0, 0))
        self.assertEqual(compare_numbers(secret_number, "1234"), (4, 0))
        self.assertEqual(compare_numbers(secret_number, "4321"), (0, 4))
        self.assertEqual(compare_numbers(secret_number, "1243"), (2, 2))

if __name__ == "__main__":
    unittest.main()
