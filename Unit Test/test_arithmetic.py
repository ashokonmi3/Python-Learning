import unittest


class TestAdditionAndSubtraction(unittest.TestCase):
    def test_addition(self):
        result = 2 + 3
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = 5 - 3
        self.assertEqual(result, 2)


class TestMultiplicationAndDivision(unittest.TestCase):
    def test_multiplication(self):
        result = 2 * 3
        self.assertEqual(result, 6)

    def test_division(self):
        result = 6 / 3
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
