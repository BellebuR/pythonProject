def modulo(a, b):
    if b == 0:
        raise ValueError("Деление на ноль недопустимо")
    return a % b

import unittest

class TestModuloFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(20, 5), 0)


    def test_zero_dividend(self):
        self.assertEqual(modulo(0, 3), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            modulo(10, 0)

if __name__ == '__main__':
    unittest.main()