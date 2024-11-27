
# Exercise 1
# In the file named tax.py the implementation of the calc_tax() function is given. Create a class named TestCalcTax that inherits from unittest.TestCase and implement the following four tests:

# test_calc_tax_twenty_percent_and_eighteen_age() - checks if for arguments:
# 60000, 0.2, 18 the return value is equal to 5000


# test_calc_tax_twenty_percent_and_nineteen_age() - checks if for arguments:
# 60000, 0.2, 19 the return value is equal to12000


# test_calc_tax_twenty_percent_and_sixty_five_age() - checks if for arguments:
# 60000, 0.2, 65 the return value is equal to 12000


# test_calc_tax_twenty_percent_and_sixty_six_age() - checks if for arguments:
# 60000, 0.2, 66 the return value is equal to 8000


# You only need to define the class and the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 1
from rectangle import area, perimeter
# from tax import calc_tax
import unittest
from tax import calculate_tax


# class TestCalcTax(unittest.TestCase):
#     def test_calc_tax_twenty_percent_and_eighteen_age(self):
#         self.assertEqual(calculate_tax(60000, 0.2, 18), 5000)

#     def test_calc_tax_twenty_percent_and_nineteen_age(self):
#         self.assertEqual(calculate_tax(60000, 0.2, 19), 12000)

#     def test_calc_tax_twenty_percent_and_sixty_five_age(self):
#         self.assertEqual(calculate_tax(60000, 0.2, 65), 12000)

#     def test_calc_tax_twenty_percent_and_sixty_six_age(self):
#         self.assertEqual(calculate_tax(60000, 0.2, 66), 8000)
# ==================================================================================

# Exercise 2
# In the file named tax.py the implementation of the calc_tax() function is given. Try to simplify the solution of the previous exercise by using parameterized tests and the unittest framework.


# Steps:

# Implement a test method named test_calc_tax() in the TestCalcTax class.

# In the test_calc_tax() method define four test cases (amount, tax_rate, age, result):


# (60000, 0.2, 18, 5000)
# (60000, 0.2, 19, 12000)
# (60000, 0.2, 65, 12000)
# (60000, 0.2, 66, 8000)


# And assign to a list named test_cases.

# Using the for loop and the context manager define the test cases as follows:


# for amount, tax_rate, age, expected in test_cases:
#     with self.subTest(
#         amount=amount,
#         tax_rate=tax_rate,
#         age=age,
#         expected=expected,
#     ):
#     pass


# You only need to define the class and the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 2


# class TestCalcTax(unittest.TestCase):
#     def test_calc_tax(self):
#         test_cases = [
#             (60000, 0.2, 18, 5000),
#             (60000, 0.2, 19, 12000),
#             (60000, 0.2, 65, 12000),
#             (60000, 0.2, 66, 8000),
#         ]
#         for amount, tax_rate, age, expected in test_cases:
#             with self.subTest(
#                 amount=amount,
#                 tax_rate=tax_rate,
#                 age=age,
#                 expected=expected,
#             ):
#                 self.assertEqual(
#                     calculate_tax(amount, tax_rate, age), expected
#                 )
# ==================================================================================

# Exercise 3
# The file rectangle.py implements three functions:

# validate_rectangle_args()

# area()

# perimeter()


# Create a class named TestArea that inherits from unittest.TestCase and implement a test method named test_area(). Using the parameterized tests in the created method, make the following assertions:

# check if calling the function area(1, 5) returns the value 5

# check if calling the function area(2, 10) returns the value 20

# check if calling the function area(100, 50) returns the value 5000


# You only need to define the class and the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


# Solution 3
# import unittest
# from rectangle import area, perimeter


# class TestArea(unittest.TestCase):
#     def test_area(self):
#         test_cases = [
#             (1, 5, 5),
#             (2, 10, 20),
#             (100, 50, 5000)
#         ]
#         for width, height, expected in test_cases:
#             with self.subTest(
#                 width=width, height=height, expected=expected
#             ):
#                 self.assertEqual(area(width, height), expected)
# ==================================================================================

# Exercise 4
# The file rectangle.py implements three functions:

# validate_rectangle_args()

# area()

# perimeter()


# Add the second test method to the TestArea class named test_area_incorrect_type_should_raise_type_error(). Using the parameterized tests in the created method, make the following assertions:

# check if calling the function area(1, '5') returns TypeError

# check if calling the function area('2', 10) returns TypeError

# check if calling the function area('two', 'four') returns TypeError


# You only need to define the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 4


# class TestArea(unittest.TestCase):
#     def test_area(self):
#         test_cases = [
#             (1, 5, 5),
#             (2, 10, 20),
#             (100, 50, 5000)
#         ]
#         for width, height, expected in test_cases:
#             with self.subTest(
#                 width=width, height=height, expected=expected
#             ):
#                 self.assertEqual(area(width, height), expected)

#     def test_area_incorrect_type_should_raise_type_error(self):
#         test_cases = [
#             (1, '5'),
#             ('2', 10),
#             ('two', 'four')
#         ]
#         for width, height in test_cases:
#             with self.subTest(width=width, height=height):
#                 with self.assertRaises(TypeError):
#                     area(width, height)
# ==================================================================================
# Exercise 5
# The file rectangle.py implements three functions:

# validate_rectangle_args()

# area()

# perimeter()


# Add the third test method to the TestArea class named test_area_invalid_value_should_raise_value_error(). Using the parameterized tests in the created method, make the following assertions:

# check if calling the function area(-4, 5) returns ValueError

# check if calling the function area(4, -5) returns ValueError

# check if calling the function area(10, 0) returns ValueError


# You only need to define the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 5
# import unittest
# from rectangle import area, perimeter


# class TestArea(unittest.TestCase):
#     def test_area_invalid_value_should_raise_value_error(self):
#         test_cases = [
#             (-4, 5),
#             (4, -5),
#             (10, 0)
#         ]
#         for width, height in test_cases:
#             with self.subTest(width=width, height=height):
#                 with self.assertRaises(ValueError):
#                     area(width, height)
# ==================================================================================

# Exercise 6
# The file rectangle.py implements three functions:

# validate_rectangle_args()

# area()

# perimeter()


# Create a class named TestPerimeter that inherits from unittest.TestCase and implement a test method named test_perimeter(). Using the parameterized tests in the created method, implement the following assertions:

# check if calling the function perimeter(1, 5) returns the value 12

# check if calling the function perimeter(2, 10) returns the value 24

# check if calling the function perimeter(100, 50) returns the value 300


# You only need to define the class and the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 6
# import unittest
# from rectangle import area, perimeter


# class TestPerimeter(unittest.TestCase):
#     def test_perimeter(self):
#         test_cases = [
#             (1, 5, 12),
#             (2, 10, 24),
#             (100, 50, 300)
#         ]
#         for width, height, expected in test_cases:
#             with self.subTest(
#                 width=width, height=height, expected=expected
#             ):
#                 self.assertEqual(perimeter(width, height), expected)
# ==================================================================================

# Exercise 7
# The file rectangle.py implements three functions:

# validate_rectangle_args()

# area()

# perimeter()


# Implement a test method called test_perimeter_invalid_type_should_raise_type_error() in the TestPerimeter class. Using the parameterized tests in the created method, implement the following assertions:

# check if calling the function perimeter(4, '5') returns TypeError

# check if calling the function perimeter('2', 8) returns TypeError

# check if calling the function perimeter('two', 'three') returns TypeError


# You only need to define the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 7
# import unittest
# from rectangle import area, perimeter


# class TestPerimeter(unittest.TestCase):
#     def test_perimeter_invalid_type_should_raise_type_error(self):
#         test_cases = [
#             (4, '5'),
#             ('2', 8),
#             ('two', 'three')
#         ]
#         for width, height in test_cases:
#             with self.subTest(width=width, height=height):
#                 with self.assertRaises(TypeError):
#                     perimeter(width, height)
# ==================================================================================

# Exercise 8
# The file rectangle.py implements three functions:

# validate_rectangle_args()

# area()

# perimeter()


# Implement a test method called test_perimeter_incorrect_value_should_raise_value_error() in the TestPerimeter class. Using the parameterized tests in the created method, implement the following assertions:

# check if calling the function perimeter(-40, 5) returns ValueError

# check if calling the function perimeter(4, -10) returns ValueError

# check if calling the function perimeter(0, 0) returns ValueError


# You only need to define the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 8
# import unittest
# from rectangle import area, perimeter


# class TestPerimeter(unittest.TestCase):
#     def test_perimeter_incorrect_value_should_raise_value_error(self):
#         invalid_cases = [
#             (-40, 5),
#             (4, -10),
#             (0, 0)
#         ]
#         for width, height in invalid_cases:
#             with self.subTest(width=width, height=height):
#                 with self.assertRaises(ValueError):
#                     perimeter(width, height)

# ==================================================================================
# Exercise 9
# Suppose you have the function that calculates the sum of the odd numbers in a list:


# def sum_odd_numbers(numbers):
#     return sum(num for num in numbers if num % 2 == 1)


# This function takes a list of integers as input, filters out the odd numbers, and returns the sum of the remaining numbers.


# Write the parameterized test using the unittest framework. Define a class called TestSumOddNumbers that inherits from unittest.TestCase. Then define five test cases:

# [1, 2, 3, 4, 5] -> 9

# [10, 11, 12, 13, 14, 15] -> 39

# [2, 4, 6] -> 0

# [] -> 0

# [1, 3, 5, 7] -> 16


# Solution 9
# import unittest


# def sum_odd_numbers(numbers):
#     return sum(num for num in numbers if num % 2 == 1)


# class TestSumOddNumbers(unittest.TestCase):
#     def test_sum_odd_numbers(self):
#         test_cases = [
#             {'input': [1, 2, 3, 4, 5], 'expected_output': 9},
#             {'input': [10, 11, 12, 13, 14, 15], 'expected_output': 39},
#             {'input': [2, 4, 6], 'expected_output': 0},
#             {'input': [], 'expected_output': 0},
#             {'input': [1, 3, 5, 7], 'expected_output': 16}
#         ]

#         for test_case in test_cases:
#             with self.subTest(test_case=test_case):
#                 input_numbers = test_case['input']
#                 expected_output = test_case['expected_output']
#                 self.assertEqual(
#                     sum_odd_numbers(input_numbers), expected_output
#                 )

# ==================================================================================

# Exercise 10
# Suppose you have the function that calculates the lengths of the strings in a list:


# def string_lengths(strings):
#     return list(map(len, strings))


# This function takes a list of strings as input, uses a map() function to calculate the length of each string, and returns a list of the resulting lengths.


# Write the parameterized test using the unittest framework. Define a class called TestStringLengths that inherits from unittest.TestCase. Then define four test cases:

# ['hello', 'world'] -> [5, 5]

# ['python', 'is', 'awesome'] -> [6, 2, 7]

# [] -> []

# ['1', '22', '333', '4444'] -> [1, 2, 3, 4]

# Solution 10
# import unittest


# def string_lengths(strings):
#     return list(map(len, strings))


# class TestStringLengths(unittest.TestCase):
#     def test_string_lengths(self):
#         test_cases = [
#             {
#                 "input": ["hello", "world"],
#                 "expected_output": [5, 5],
#             },
#             {
#                 "input": ["python", "is", "awesome"],
#                 "expected_output": [6, 2, 7],
#             },
#             {
#                 "input": [],
#                 "expected_output": []
#             },
#             {
#                 "input": ["1", "22", "333", "4444"],
#                 "expected_output": [1, 2, 3, 4],
#             },
#         ]

#         for test_case in test_cases:
#             with self.subTest(test_case=test_case):
#                 input_strings = test_case["input"]
#                 expected_output = test_case["expected_output"]
#                 self.assertEqual(
#                     string_lengths(input_strings),
#                     expected_output,
#                 )
# ==================================================================================
# Exercise 11
# Suppose you have the function that calculates the quotient of the first number divided by the second number:


# def quotient(numbers):
#     if numbers[1] == 0:
#         raise ValueError('Division by zero')
#     return numbers[0] / numbers[1]


# This function takes a list of two integers as input, checks if the second integer is zero, and raises a ValueError if it is. Otherwise, it returns the quotient of the first integer divided by the second integer.


# Write the parameterized test using the unittest framework. Define a class called TestQuotient that inherits from unittest.TestCase. Then define six test cases:

# [1, 2] -> 0.5

# [10, 5] -> 2

# [2, 0] -> None

# [-10, 5] -> -2

# [0, 1] -> 0

# [0, 0] -> None

# Solution 11


# def quotient(numbers):
#     if numbers[1] == 0:
#         raise ValueError('Division by zero')
#     return numbers[0] / numbers[1]


# class TestQuotient(unittest.TestCase):
#     def test_quotient(self):
#         test_cases = [
#             {'input': [1, 2], 'expected_output': 0.5},
#             {'input': [10, 5], 'expected_output': 2},
#             {'input': [2, 0], 'expected_output': None},
#             {'input': [-10, 5], 'expected_output': -2},
#             {'input': [0, 1], 'expected_output': 0},
#             {'input': [0, 0], 'expected_output': None}
#         ]

#         for test_case in test_cases:
#             with self.subTest(test_case=test_case):
#                 if test_case["input"][1] == 0:
#                     self.assertRaises(
#                         ValueError, quotient, test_case["input"]
#                     )
#                 else:
#                     self.assertEqual(
#                         quotient(test_case["input"]),
#                         test_case["expected_output"],
#                     )

# ==================================================================================

# Exercise 12
# Suppose you have the function that removes all vowels from a string:


# def remove_vowels(input_str):
#     if not isinstance(input_str, str):
#         raise TypeError("Input must be a string")
#     vowels = ["a", "e", "i", "o", "u"]
#     return "".join(
#         [char for char in input_str if char.lower() not in vowels]
#     )


# This function takes a string as input, checks if the input is a string using the isinstance() function, and raises a TypeError if it is not. It then defines a list of vowels, uses a list comprehension to remove all vowels from the input string, and returns the resulting string.


# Write the parameterized test using the unittest framework. Define a class called TestRemoveVowels that inherits from unittest.TestCase. Then define five test cases:

# "hello world" -> "hll wrld"

# "Python is awesome" -> "Pythn s wsm"

# "aeiou" -> ""

# "" -> ""

# ["not a string"] -> None

# {"not a string": "value"} -> None

# None -> None

# Solution 12
# import unittest


# def remove_vowels(input_str):
#     if not isinstance(input_str, str):
#         raise TypeError("Input must be a string")
#     vowels = ["a", "e", "i", "o", "u"]
#     return "".join(
#         [char for char in input_str if char.lower() not in vowels]
#     )


# class TestRemoveVowels(unittest.TestCase):
#     def test_remove_vowels(self):
#         test_cases = [
#             {
#                 "input": "hello world",
#                 "expected_output": "hll wrld",
#             },
#             {
#                 "input": "Python is awesome",
#                 "expected_output": "Pythn s wsm",
#             },
#             {
#                 "input": "aeiou",
#                 "expected_output": "",
#             },
#             {
#                 "input": "",
#                 "expected_output": "",
#             },
#             {
#                 "input": ["not a string"],
#                 "expected_output": None,
#             },
#             {
#                 "input": {
#                     "not a string": "value"
#                 },
#                 "expected_output": None,
#             },
#             {
#                 "input": None,
#                 "expected_output": None,
#             },
#         ]

#         for test_case in test_cases:
#             with self.subTest(test_case=test_case):
#                 if not isinstance(test_case["input"], str):
#                     self.assertRaises(
#                         TypeError,
#                         remove_vowels,
#                         test_case["input"],
#                     )
#                 else:
#                     self.assertEqual(
#                         remove_vowels(test_case["input"]),
#                         test_case["expected_output"],
#                     )

# ==================================================================================
# Exercise 13
# Suppose you have the function that reverses the keys and values in a dictionary:


# def reverse_dict(input_dict):
#     if not isinstance(input_dict, dict):
#         raise TypeError("Input must be a dictionary")
#     for key, value in input_dict.items():
#         if not isinstance(value, int):
#             raise ValueError("All values must be integers")
#     return {value: key for key, value in input_dict.items()}


# This function takes a dictionary with string keys and integer values as input, checks if the input is a dictionary using the isinstance function, and raises a TypeError if it is not. It then checks if all values in the dictionary are integers, and raises a ValueError if any of them are not. It then creates a new dictionary with the keys and values reversed using a dictionary comprehension, and returns the new dictionary.


# Write the parameterized test using the unittest framework. Define a class called TestReverseDict that inherits from unittest.TestCase. Then define the following test cases:

# {"one": 1, "two": 2, "three": 3} -> {1: "one", 2: "two", 3: "three"}

# {"a": 0, "b": -1, "c": 10} -> {0: "a", -1: "b", 10: "c"}

# {} -> {}

# {"one": "1", "two": 2, "three": 3} -> None

# ["not a dictionary"] -> None

# {"one": 1, "two": "2", "three": 3} -> None

# {"one": 1, "two": 2, "three": "3"} -> None

# {"one": 1, "two": 2, 3: "three"} -> None

# Solution 13
# import unittest


# def reverse_dict(input_dict):
#     if not isinstance(input_dict, dict):
#         raise TypeError("Input must be a dictionary")
#     for key, value in input_dict.items():
#         if not isinstance(value, int):
#             raise ValueError("All values must be integers")
#     return {value: key for key, value in input_dict.items()}


# class TestReverseDict(unittest.TestCase):
#     def test_reverse_dict(self):
#         test_cases = [
#             {
#                 "input": {"one": 1, "two": 2, "three": 3},
#                 "expected_output": {1: "one", 2: "two", 3: "three"},
#             },
#             {
#                 "input": {"a": 0, "b": -1, "c": 10},
#                 "expected_output": {0: "a", -1: "b", 10: "c"},
#             },
#             {"input": {}, "expected_output": {}},
#             {
#                 "input": {"one": "1", "two": 2, "three": 3},
#                 "expected_output": None,
#             },
#             {
#                 "input": ["not a dictionary"],
#                 "expected_output": None,
#             },
#             {
#                 "input": {"one": 1, "two": "2", "three": 3},
#                 "expected_output": None,
#             },
#             {
#                 "input": {"one": 1, "two": 2, "three": "3"},
#                 "expected_output": None,
#             },
#             {
#                 "input": {"one": 1, "two": 2, 3: "three"},
#                 "expected_output": None,
#             },
#         ]

#         for test_case in test_cases:
#             with self.subTest(test_case=test_case):
#                 if not isinstance(test_case["input"], dict):
#                     self.assertRaises(
#                         TypeError,
#                         reverse_dict,
#                         test_case["input"],
#                     )
#                 elif not all(
#                     isinstance(value, int)
#                     for value in test_case["input"].values()
#                 ):
#                     self.assertRaises(
#                         ValueError,
#                         reverse_dict,
#                         test_case["input"],
#                     )
#                 else:
#                     self.assertEqual(
#                         reverse_dict(test_case["input"]),
#                         test_case["expected_output"],
#                     )


# =======================================================================================
if __name__ == '__main__':
    unittest.main(verbosity=2)
