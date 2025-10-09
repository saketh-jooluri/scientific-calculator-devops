# tests/test_calculator.py
import unittest
from app.calculator import sqrt, factorial, ln, power

class TestCalculator(unittest.TestCase):
    def test_sqrt_basic(self):
        self.assertAlmostEqual(sqrt(9), 3.0)
        self.assertAlmostEqual(sqrt(2), 2**0.5)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_factorial_basic(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_type(self):
        with self.assertRaises(TypeError):
            factorial(5.5)

    def test_ln_basic(self):
        import math
        self.assertAlmostEqual(ln(math.e), 1.0)
        self.assertAlmostEqual(ln(1), 0.0)

    def test_ln_negative(self):
        with self.assertRaises(ValueError):
            ln(-1)

    def test_power(self):
        self.assertAlmostEqual(power(2, 3), 8.0)
        self.assertAlmostEqual(power(9, 0.5), 3.0)

if __name__ == "__main__":
    unittest.main()
