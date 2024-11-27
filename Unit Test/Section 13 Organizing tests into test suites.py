

# Exercise 1
# Suppose you have the following code:


# import unittest


# def calculate_rectangle_area(length, width):
#     return length * width

# def calculate_square_area(side_length):
#     return side_length ** 2


# class TestAreaFunctions(unittest.TestCase):
#     def test_rectangle_area(self):
#         self.assertEqual(calculate_rectangle_area(5, 10), 50)
#         self.assertEqual(calculate_rectangle_area(3, 4), 12)

#     def test_square_area(self):
#         self.assertEqual(calculate_square_area(5), 25)
#         self.assertEqual(calculate_square_area(2), 4)


# Create a TestSuite object and add these two test cases to it. Then, run the TestSuite to ensure that both functions pass their unit tests.

# Solution 1
import unittest


# def calculate_rectangle_area(length, width):
#     return length * width


# def calculate_square_area(side_length):
#     return side_length ** 2


# class TestAreaFunctions(unittest.TestCase):
#     def test_rectangle_area(self):
#         self.assertEqual(calculate_rectangle_area(5, 10), 50)
#         self.assertEqual(calculate_rectangle_area(3, 4), 12)

#     def test_square_area(self):
#         self.assertEqual(calculate_square_area(5), 25)
#         self.assertEqual(calculate_square_area(2), 4)


# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(TestAreaFunctions('test_rectangle_area'))
#     suite.addTest(TestAreaFunctions('test_square_area'))
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
# ==================================================================================

# Exercise 2
# Suppose you have the following code:


# import unittest


# def reverse_string(string):
#     return string[::-1]


# def remove_vowels(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     result = ""
#     for letter in string:
#         if letter.lower() not in vowels:
#             result += letter
#     return result


# def capitalize_first_letter(string):
#     return string.capitalize()


# class TestStringManipulationFunctions(unittest.TestCase):
#     def test_reverse_string(self):
#         self.assertEqual(reverse_string('hello'), 'olleh')
#         self.assertEqual(reverse_string('world'), 'dlrow')

#     def test_remove_vowels(self):
#         self.assertEqual(remove_vowels('hello world'), 'hll wrld')
#         self.assertEqual(remove_vowels('python is awesome'), 'pythn s wsm')

#     def test_capitalize_first_letter(self):
#         self.assertEqual(capitalize_first_letter('hello'), 'Hello')
#         self.assertEqual(capitalize_first_letter('world'), 'World')


# Create a TestSuite object and add these three test cases to it. Then, run the TestSuite to ensure that both functions pass their unit tests.

# Solution 2
# import unittest


# def reverse_string(string):
#     return string[::-1]


# def remove_vowels(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     result = ""
#     for letter in string:
#         if letter.lower() not in vowels:
#             result += letter
#     return result


# def capitalize_first_letter(string):
#     return string.capitalize()


# class TestStringManipulationFunctions(unittest.TestCase):
#     def test_reverse_string(self):
#         self.assertEqual(reverse_string('hello'), 'olleh')
#         self.assertEqual(reverse_string('world'), 'dlrow')

#     def test_remove_vowels(self):
#         self.assertEqual(remove_vowels('hello world'), 'hll wrld')
#         self.assertEqual(remove_vowels('is awesome'), 's wsm')

#     def test_capitalize_first_letter(self):
#         self.assertEqual(capitalize_first_letter('hello'), 'Hello')
#         self.assertEqual(capitalize_first_letter('world'), 'World')


# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(
#         TestStringManipulationFunctions('test_reverse_string')
#     )
#     suite.addTest(
#         TestStringManipulationFunctions('test_remove_vowels')
#     )
#     suite.addTest(
#         TestStringManipulationFunctions('test_capitalize_first_letter')
#     )
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
# ==================================================================================
# Exercise 3
# Suppose you have a simple calculator.py module. This module defines basic arithmetic functions.


# Also, you have created two separate test classes in the test_aritmetic.py file. One for testing addition and subtraction, and another for testing multiplication and division.


# Your task is to organize these two classes into a test suite using the TestSuite class from the unittest module and run the given tests.


# Solution 3
# import unittest
# from test_arithmetic import TestAdditionAndSubtraction
# from test_arithmetic import TestMultiplicationAndDivision


# suite = unittest.TestSuite()

# suite.addTest(unittest.makeSuite(TestAdditionAndSubtraction))
# suite.addTest(unittest.makeSuite(TestMultiplicationAndDivision))

# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suite)


# ==================================================================================
# Exercise 4
# Suppose you have a simple animal.py module. This module defines an Animal class and two subclasses, Cat and Dog. Each subclass overrides the make_sound() method of the Animal class.


# Also, you have created two separate test classes in the test_animals.py file. One for testing the Cat class and another for testing the Dog class.


# Your task is to organize these two classes into a test suite using the TestSuite class from the unittest module and run the given tests.

# Solution 4
import unittest
from test_animals import TestCats, TestDogs


suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestCats))
suite.addTest(unittest.makeSuite(TestDogs))

runner = unittest.TextTestRunner()
runner.run(suite)

# ==================================================================================
