import unittest

# - Create a class which contains all our test cases
# - The class will import unittest.TestCase
# - Each function in the class will be treated as a test case, its should start with keyword test_***
# - Use asserstion in the test case to decide the test results.


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()

# python -m unittest .\01_unit_test.py
# python -m unittest -v 01_unit_test.py
# python -m unittest 01_unit_test.TestStringMethods.test_split
# python - m unittest or python -m unittest discover (only test*.py)
