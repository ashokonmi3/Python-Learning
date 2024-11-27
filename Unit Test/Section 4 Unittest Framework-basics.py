# Exercise 1
# Using the unittest framework, create a TestSplitMethod class that inherits from the unittest.TestCase
#  class and implements the following three tests:

# test_split_by_default()

# test that checks if the code 'Python Testing'.split() returns a list
# ['Python', 'Testing']


# test_split_by_comma()

# test that checks if the code 'open,high,low,close'.split(',') returns a list ['open', 'high', 'low', 'close']


# test_split_by_hash()

# test that checks if the code 'summer#time#vibes'.split('#') returns a list ['summer', 'time', 'vibes']

# Solution 1
import unittest


# class TestSplitMethod(unittest.TestCase):
#     def test_split_by_default(self):
#         self.assertEqual('Python Testing'.split(), ['Python', 'Testing'])

#     def test_split_by_comma(self):
#         actual = 'open,high,low,close'.split(',')
#         expected = ['open', 'high', 'low', 'close']
#         self.assertEqual(actual, expected)

#     def test_split_by_hash(self):
#         actual = 'summer#time#vibes'.split('#')
#         expected = ['summer', 'time', 'vibes']
#         self.assertEqual(actual, expected)


# if __name__ == '__main__':
#     unittest.main()
# ==========================================================================================
# Exercise 2
# Using the unittest framework, create a TestJoinMethod class that inherits from the unittest.TestCase class and implements the following three tests:

# test_join_with_space()

# test that checks if the code ' '.join(['Python', '3.8']) returns a list
# 'Python 3.8'


# test_join_with_comma()

# test that checks if the code ','.join(['open', 'high', 'low', 'close']) returns a list 'open,high,low,close'


# test_join_with_new_line_char()

# test that checks if the code '\n'.join(['open', 'high', 'low', 'close']) returns a list 'open\nhigh\nlow\nclose'

# Solution 2
# import unittest

# # split --> convert a string to list
# # Join --> list to string
# class TestJoinMethod(unittest.TestCase):
#     def test_join_with_space(self):
#         self.assertEqual(' '.join(['Python', '3.8']), 'Python 3.8')

#     def test_join_with_comma(self):
#         actual = ','.join(['open', 'high', 'low', 'close'])
#         expected = 'open,high,low,close'
#         self.assertEqual(actual, expected)

#     def test_join_with_new_line_char(self):
#         actual = '\n'.join(['open', 'high', 'low', 'close'])
#         expected = 'open\nhigh\nlow\nclose'
#         self.assertEqual(actual, expected)


# if __name__ == '__main__':
#     unittest.main()


# ==========================================================================================
# Exercise 3
# Using the unittest framework, the TestJoinMethod class was created. The class has the following three tests:

# test_join_with_space()

# test that checks if the code ' '.join(['Python', '3.8']) returns a list
# 'Python 3.8'


# test_join_with_comma()

# test that checks if the code ','.join(['open', 'high', 'low', 'close']) returns a list 'open,high,low,close'


# test_join_with_new_line_char()

# test that checks if the code '\n'.join(['open', 'high', 'low', 'close']) returns a list 'open\nhigh\nlow\nclose'

# Solution 3
# import unittest


# class TestJoinMethod(unittest.TestCase):
#     def test_join_with_space(self):
#         self.assertEqual(' '.join(['Python', '3.8']), 'Python 3.8')

#     def test_join_with_comma(self):
#         actual = ','.join(['open', 'high', 'low', 'close'])
#         expected = 'open,high,low,close'
#         self.assertEqual(actual, expected)

#     def test_join_with_new_line_char(self):
#         actual = '\n'.join(['open', 'high', 'low', 'close'])
#         expected = 'open\nhigh\nlow\nclose'
#         self.assertEqual(actual, expected)


# if __name__ == '__main__':
#     unittest.main()

# =======================================================================================================
# Exercise 4
# The following TestIsInstance class is given:


# import unittest
# from collections import Counter


# class TestIsInstance(unittest.TestCase):
#     def test_case_1(self):
#         self.assertTrue(isinstance((), tuple))

#     def test_case_2(self):
#         self.assertTrue(isinstance([], list))

#     def test_case_3(self):
#         self.assertTrue(isinstance({}, dict))

#     def test_case_4(self):
#         cnt = Counter()
#         self.assertTrue(isinstance(cnt, Counter))

#     def test_case_5(self):
#         var1 = 4
#         self.assertTrue(isinstance(var1, int))


# Add one more test named test_case_6() that checks the type of var2 (note the comma after the number 4):


# var2 = 4,


# Then run all tests.

# Solution 4
# import unittest
# from collections import Counter


# class TestIsInstance(unittest.TestCase):
#     def test_case_1(self):
#         self.assertTrue(isinstance((), tuple))

#     def test_case_2(self):
#         self.assertTrue(isinstance([], list))

#     def test_case_3(self):
#         self.assertTrue(isinstance({}, dict))

#     def test_case_4(self):
#         cnt = Counter()
#         self.assertTrue(isinstance(cnt, Counter))

#     def test_case_5(self):
#         var1 = 4
#         self.assertTrue(isinstance(var1, int))

#     def test_case_6(self):
#         var2 = 4,
#         self.assertTrue(isinstance(var2, tuple))


# if __name__ == '__main__':
#     unittest.main()
#     =====================================================================================

#     Exercise 5
# Using the unittest framework create a TestUpper class that inherits from the unittest.TestCase class and implements the following two tests:

# test_upper()

# test that checks if the code  'summer'.upper() returns string 'SUMMER'


# test_is_upper()

# test that checks if the code 'SUMMER'.isupper() returns the boolean value True

# test that checks if the code 'summer'.isupper() returns the boolean value False


# You only need to define the class and the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.
# Solution 5
# import unittest


# class TestUpper(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('summer'.upper(), 'SUMMER')

#     def test_is_upper(self):
#         self.assertTrue('SUMMER'.isupper())
#         self.assertFalse('summer'.isupper())


# if __name__ == '__main__':
#     unittest.main()
#     ========================================================================================
#    Exercise 6
# Using the unittest framework create a TestLower class that inherits from the unittest.TestCase class and implements the following two tests:

# test_lower()

# test that checks if the code 'Joe.Smith@mail.com'.lower() returns string 'joe.smith@mail.com'


# test_is_lower()

# test that checks if the code 'joe.smith@mail.com'.islower() returns the boolean value True

# test that checks if the code 'Joe.Smith@mail.com'.islower() returns the boolean value False


# You only need to define the class and the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.
# Solution 6
# import unittest


# class TestLower(unittest.TestCase):
#     def test_lower(self):
#         self.assertEqual(
#             'Joe.Smith@mail.com'.lower(), 'joe.smith@mail.com'
#         )

#     def test_is_lower(self):
#         self.assertTrue('joe.smith@mail.com'.islower())
#         self.assertFalse('Joe.Smith@mail.com'.islower())


# if __name__ == '__main__':
#     unittest.main()
#     ============================================================================================
#     Exercise 7
# Using the unittest framework create two classes named: TestStartsWithMethod and TestEndsWithMethod that inherit from the unittest.TestCase class.


# The TestStartsWithMethod class implements two test methods:

# test_startswith_one_letter()

# test that checks if the code 'unittest'.startswith('u') returns the boolean value True

# test that checks if the code 'unittest'.startswith('U') returns the boolean value False


# test_startswith_four_letters()

# test that checks if the code 'http://www.e-smartdata.org/'.startswith('http') returns the boolean value True

# test that checks if the code 'www.e-smartdata.org/'.startswith('http') returns the boolean value False


# The TestEndsWithMethod class implements one test method:

# test_endswith_three_letter()

# test that checks if the code 'e-smartdata.org'.endswith('org') returns the boolean value True

# test that checks if the code 'e-smartdata.org'.endswith('com') returns the boolean value False


# You only need to define classes and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 7
# import unittest


# class TestStartsWithMethod(unittest.TestCase):
#     def test_startswith_one_letter(self):
#         self.assertTrue('unittest'.startswith('u'))
#         self.assertFalse('unittest'.startswith('U'))

#     def test_startswith_four_letters(self):
#         self.assertTrue('http://www.e-smartdata.org/'.startswith('http'))
#         self.assertFalse('www.e-smartdata.org/'.startswith('http'))


# class TestEndsWithMethod(unittest.TestCase):

#     def test_endswith_three_letter(self):
#         self.assertTrue('e-smartdata.org'.endswith('org'))
#         self.assertFalse('e-smartdata.org'.endswith('com'))


# if __name__ == '__main__':
#     unittest.main()
#     ====================================================================================================
#     Exercise 8
# Using the unittest framework create three classes named: TestLstripMethod, TestStripMethod and TestRstripMethod that inherit from the unittest.TestCase class. Then add two test methods to each class, testing the behavior of the methods appropriately:

# str.lstrip()

# str.strip()

# str.rstrip()


# Choose appropriate names for the test cases and test methods at your discretion.
# Solution 8
# import unittest


# class TestLstripMethod(unittest.TestCase):
#     def test_lstrip_with_space(self):
#         self.assertEqual('  price,volume  '.lstrip(), 'price,volume  ')

#     def test_lstrip_with_new_line_char(self):
#         self.assertEqual('\nprice,volume\n'.lstrip(), 'price,volume\n')


# class TestStripMethod(unittest.TestCase):
#     def test_strip_with_space(self):
#         self.assertEqual('  price,volume  '.strip(), 'price,volume')

#     def test_strip_with_new_line_char(self):
#         self.assertEqual('\nprice,volume\n'.strip(), 'price,volume')


# class TestRstripMethod(unittest.TestCase):
#     def test_rstrip_with_space(self):
#         self.assertEqual('  price,volume  '.rstrip(), '  price,volume')

#     def test_rstrip_with_new_line_char(self):
#         self.assertEqual('\nprice,volume\n'.rstrip(), '\nprice,volume')

# ==================================================================================
# Exercise 9
# Suppose you have the StringReverser class with the reverse method:


# class StringReverser:
#     def reverse(self, string):
#         return string[::-1]


# Create the unit test class named TestStringReverser and define the test cases.
# The test_reverse() method should test the reverse() method of the StringReverser class by creating a
# new instance of the class, calling the reverse() method with different strings,
#  and checking that the return value matches the expected result using the assertEqual() method.

# Test the reverse() method with three different strings:

# "hello"

# "12345"

# "" (empty string)


# The expected results are "olleh", "54321", and "", respectively.
# Solution 9
# import unittest


# class StringReverser:
#     def reverse(self, string):
#         return string[::-1]


# class TestStringReverser(unittest.TestCase):
#     def test_reverse(self):
#         # Create a new instance of the StringReverser class
#         reverser = StringReverser()

#         # Test that "hello" reversed is "olleh"
#         self.assertEqual(reverser.reverse("hello"), "olleh")

#         # Test that "12345" reversed is "54321"
#         self.assertEqual(reverser.reverse("12345"), "54321")

#         # Test that "" (empty string) reversed is ""
#         self.assertEqual(reverser.reverse(""), "")

# ==================================================================================
# Suppose you have the Rectangle class with the area() method:


# class Rectangle:
#     def __init__(self, width: float, height: float) -> None:
#         self._validate_params(width, height)
#         self.width = width
#         self.height = height

#     def _validate_params(self, width: float, height: float) -> None:
#         if not isinstance(width, (int, float)) or width < 0:
#             raise ValueError("Width must be a positive number")
#         if not isinstance(height, (int, float)) or height < 0:
#             raise ValueError("Height must be a positive number")

#     def area(self) -> float:
#         return self.width * self.height


# Create the unit test class named TestRectangle and define the test cases:

# test_area_with_nonzero_dimensions()

# test_area_with_zero_dimensions()

# test_area_with_negative_width()

# test_area_with_negative_height()

# test_area_with_float_dimensions()

# test_area_with_large_dimensions()


# In the test_area() method tests the area() method of the Rectangle class
# by creating a new instance of the class with three different width and height values,
# calling the area() method, and checking that the return value matches the expected result using the assertEqual() method.

# Solution 10
# import unittest


# class Rectangle:
#     def __init__(self, width: float, height: float) -> None:
#         self._validate_params(width, height)
#         self.width = width
#         self.height = height

#     def _validate_params(self, width: float, height: float) -> None:
#         if not isinstance(width, (int, float)) or width < 0:
#             raise ValueError("Width must be a positive number")
#         if not isinstance(height, (int, float)) or height < 0:
#             raise ValueError("Height must be a positive number")

#     def area(self) -> float:
#         return self.width * self.height


# class TestRectangle(unittest.TestCase):
#     def test_area_with_nonzero_dimensions(self):
#         rect = Rectangle(4, 5)
#         self.assertEqual(rect.area(), 20)

#     def test_area_with_zero_dimensions(self):
#         rect = Rectangle(0, 0)
#         self.assertEqual(rect.area(), 0)

#     def test_area_with_negative_width(self):
#         with self.assertRaises(ValueError):
#             rect = Rectangle(-4, 5)

#     def test_area_with_negative_height(self):
#         with self.assertRaises(ValueError):
#             rect = Rectangle(4, -5)

#     def test_area_with_float_dimensions(self):
#         rect = Rectangle(3.5, 2.5)
#         self.assertEqual(rect.area(), 8.75)

#     def test_area_with_large_dimensions(self):
#         rect = Rectangle(1000000, 1000000)
#         self.assertEqual(rect.area(), 1000000000000)

# ==================================================================================
# Exercise 11
# Suppose you have the TemperatureConverter class with the celsius_to_fahrenheit method:


# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius: float) -> float:
#         return (celsius * 9 / 5) + 32


# Create the unit test class named TestTemperatureConverter and define the test cases.

# In the test_celsius_to_fahrenheit() method tests the celsius_to_fahrenheit() static method of the TemperatureConverter class by creating a new instance of the class, calling the celsius_to_fahrenheit() method with three different temperature values in Celsius, and checking that the return value matches the expected result using the assertAlmostEqual() method.

# Solution 11
# import unittest


# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius: float) -> float:
#         return (celsius * 9 / 5) + 32


# class TestTemperatureConverter(unittest.TestCase):
#     def test_celsius_to_fahrenheit(self) -> None:
#         c = TemperatureConverter()
#         # Test that 0 degrees Celsius is 32 degrees Fahrenheit
#         self.assertAlmostEqual(
#             c.celsius_to_fahrenheit(0), 32, delta=0.5
#         )

#         # Test that 100 degrees Celsius is 212 degrees Fahrenheit
#         self.assertAlmostEqual(
#             c.celsius_to_fahrenheit(100), 212, delta=0.5
#         )

#         # Test that -40 degrees Celsius is -40 degrees Fahrenheit
#         self.assertAlmostEqual(
#             c.celsius_to_fahrenheit(-40), -40, delta=0.5
#         )

# ==================================================================================

# Exercise 12
# Suppose you have a function called calculate_average() that takes a list of numbers as input and returns the average of those numbers. Your task is to write test cases for this function using unittest.


# Here's an example implementation of the calculate_average() function:


# def calculate_average(numbers):
#     if not numbers:
#         return None
#     return sum(numbers) / len(numbers)


# Using the unittest framework create the unit test class named TestCalculateAverage and implement the following test cases:

# test_calculate_average_valid_input() - 3 different assertions

# test_calculate_average_empty_input() - 1 assertion

# test_calculate_average_invalid_input() - 3 different assertions


# Choose the input data for the tests according to the description of the test methods. You should use a total of 7 assertion methods.
# Solution 12
# import unittest


# def calculate_average(numbers):
#     if not numbers:
#         return None
#     return sum(numbers) / len(numbers)


# class TestCalculateAverage(unittest.TestCase):
#     def test_calculate_average_valid_input(self):
#         self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)
#         self.assertEqual(calculate_average([2.5, 3.5, 4.5]), 3.5)
#         self.assertEqual(calculate_average([-2, 0, 2]), 0)

#     def test_calculate_average_empty_input(self):
#         self.assertEqual(calculate_average([]), None)

#     def test_calculate_average_invalid_input(self):
#         self.assertRaises(TypeError, calculate_average, [1, 2, "3", 5])
#         self.assertRaises(TypeError, calculate_average, ["a", "b", "c"])
#         self.assertRaises(TypeError, calculate_average, [None, None])

# ==================================================================================

# Exercise 13
# Suppose you have a function called find_largest() that takes a list of integers as input and returns the largest integer in the list. Your task is to write test cases for this function using unittest.


# Here's an example implementation of the find_largest() function:


# def find_largest(numbers):
#     if not isinstance(numbers, list):
#         raise TypeError("Input must be a list")
#     if not all(isinstance(num, (int, float)) for num in numbers):
#         raise TypeError("All elements in the list must be numbers")
#     if not numbers:
#         return None
#     largest = numbers[0]
#     for num in numbers:
#         if num > largest:
#             largest = num
#     return largest


# Using the unittest framework create the unit test class named TestFindLargest and implement the following test cases:

# test_find_largest_valid_input() - 3 different assertions

# test_find_largest_empty_input() - 1 assertion

# test_find_largest_invalid_input() - 3 different assertions


# Choose the input data for the tests according to the description of the test methods. You should use a total of 7 assertion methods.
# Solution 13
# import unittest


# def find_largest(numbers):
#     if not isinstance(numbers, list):
#         raise TypeError("Input must be a list")
#     if not all(isinstance(num, (int, float)) for num in numbers):
#         raise TypeError("All elements in the list must be numbers")
#     if not numbers:
#         return None
#     largest = numbers[0]
#     for num in numbers:
#         if num > largest:
#             largest = num
#     return largest


# class TestFindLargest(unittest.TestCase):
#     def test_find_largest_valid_input(self):
#         self.assertEqual(find_largest([1, 2, 3, 4, 5]), 5)
#         self.assertEqual(find_largest([2, -3, 4, 0, -1]), 4)
#         self.assertEqual(find_largest([-2, -5, -3]), -2)

#     def test_find_largest_empty_input(self):
#         self.assertEqual(find_largest([]), None)

#     def test_find_largest_invalid_input(self):
#         self.assertRaises(TypeError, find_largest, [1, 2, "3", 4, 5])
#         self.assertRaises(TypeError, find_largest, ["a", "b", "c"])
#         self.assertRaises(TypeError, find_largest, [None, True])

# ==================================================================================
