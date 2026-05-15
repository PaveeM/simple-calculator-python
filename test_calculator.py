import unittest
from calculator import add, subtract, multiply, divide, power, square_root, percentage

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(10, -1), 0.1)

    def test_square_root(self):
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_percentage(self):
        self.assertEqual(percentage(500, 20), 100)
        self.assertEqual(percentage(100, 7), 7)
        self.assertEqual(percentage(0, 50), 0)

if __name__ == "__main__":
    unittest.main()
