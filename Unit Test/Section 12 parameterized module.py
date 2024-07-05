
# Exercise 1
# Suppose you have the function that calculates the sum of the even numbers in a list:


# def sum_even_numbers(numbers):
#     return sum(filter(lambda x: x % 2 == 0, numbers))


# This function takes a list of integers as input, filters out the odd numbers using the filter function and a
# lambda expression, and returns the sum of the even numbers.


# Use the parameterized library to write a parameterized test for the sum_even_numbers() function.


# Test the sum_even_numbers() function with five different input lists:

# [1, 2, 3, 4, 5]

# [10, 20, 30, 40, 50]

# [1, 3, 5, 7, 9]

# [0, 2, 4, 6, 8]

# []


# For each input list, you should also specify the expected output.


# Tip: Use the @parameterized.expand decorator to create a separate test case for each set of input.

# Solution 1
import unittest
from parameterized import parameterized


# def sum_even_numbers(numbers):
#     return sum(filter(lambda x: x % 2 == 0, numbers))


# class TestSumEvenNumbers(unittest.TestCase):
#     @parameterized.expand([
#         ([1, 2, 3, 4, 5], 6),
#         ([10, 20, 30, 40, 50], 150),
#         ([1, 3, 5, 7, 9], 0),
#         ([0, 2, 4, 6, 8], 20),
#         ([], 0)
#     ])
#     def test_sum_even_numbers(self, input_list, expected_output):
#         self.assertEqual(sum_even_numbers(input_list), expected_output)
# ==================================================================================

# Exercise 2
# Suppose you have the function that reverses a string:


# def reverse_string(input_str):
#     return input_str[::-1]


# This function takes a string as input and returns the reverse of the string using slicing.


# Use the parameterized library to write a parameterized test for the reverse_string() function.


# Test the reverse_string() function with five different input lists:

# "hello"

# "python"

# "racecar"

# "12345"

# "" (empty string)


# For each input list, you should also specify the expected output.


# Tip: Use the @parameterized.expand decorator to create a separate test case for each set of input.

# Solution 2
# import unittest
# from parameterized import parameterized


# def reverse_string(input_str):
#     return input_str[::-1]


# class TestReverseString(unittest.TestCase):
#     @parameterized.expand([
#         ("hello", "olleh"),
#         ("python", "nohtyp"),
#         ("racecar", "racecar"),
#         ("12345", "54321"),
#         ("", "")
#     ])
#     def test_reverse_string(self, input_str, expected_output):
#         self.assertEqual(reverse_string(input_str), expected_output)
# ==================================================================================
# Exercise 3
# Suppose you have the function that creates a list of tuples containing each integer and its square:


# def square_pairs(numbers):
#     return [(x, x**2) for x in numbers]


# This function takes a list of integers as input and returns a list of tuples containing each integer and its square. We use a list comprehension to create the list of tuples.


# Use the parameterized library to write a parameterized test for the square_pairs() function.


# Test the square_pairs() function with five different input lists:

# [1, 2, 3, 4, 5] -> [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# [-1, 0, 1] -> [(-1, 1), (0, 0), (1, 1)]

# [] -> []

# [2**31-1] ->  [(2**31-1, (2**31-1)**2)


# For each input list, you should also specify the expected output.


# Tip: Use the @parameterized.expand decorator to create a separate test case for each set of input.

# Solution 3
# import unittest
# from parameterized import parameterized


# def square_pairs(numbers):
#     return [(x, x**2) for x in numbers]


# class TestSquarePairs(unittest.TestCase):
#     @parameterized.expand([
#         ([1, 2, 3, 4, 5], [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]),
#         ([-1, 0, 1], [(-1, 1), (0, 0), (1, 1)]),
#         ([], []),
#         ([2**31-1], [(2**31-1, (2**31-1)**2)])
#     ])
#     def test_square_pairs(self, input_list, expected_output):
#         self.assertEqual(square_pairs(input_list), expected_output)
# ==================================================================================
# Exercise 4
# Suppose you have the function that calculates the average of a list of numbers:


# def average(numbers):
#     if not isinstance(numbers, list):
#         raise TypeError("Input must be a list")
#     if len(numbers) == 0:
#         raise ValueError("List must not be empty")
#     return sum(numbers) / len(numbers)


# This function takes a list of numbers as input, checks if the input is a list using the isinstance function, and raises a TypeError if it is not. It then checks if the input list is empty using the len function, and raises a ValueError if it is. It then calculates the average of the numbers in the list and returns the result.


# Use the parameterized library to write a parameterized test for the average() function.


# Test the average() function with the following different input lists:

# [1, 2, 3] -> 2

# [10, 20, 30, 40] -> 25

# [5] -> 5

# [0, 0, 0] -> 0

# [] -> None

# ["not a number"] -> None

# ["1", 2, 3] -> None

# [None] -> None


# Tip: You should use the parameterized.expand decorator to create a parameterized test. The decorator takes a list of tuples, each containing the input list and the expected output. The expand function expands each tuple into a separate test case with the input list and expected output as arguments.

# Solution 4
# import unittest
# from parameterized import parameterized


# class TestAverage(unittest.TestCase):
#     @parameterized.expand(
#         [
#             ([1, 2, 3], 2),
#             ([10, 20, 30, 40], 25),
#             ([5], 5),
#             ([0, 0, 0], 0),
#             ([], None),
#             (["not a number"], None),
#             (["1", 2, 3], None),
#             ([None], None),
#         ]
#     )
#     def test_average(self, input_list, expected_output):
#         if expected_output is None:
#             with self.assertRaises((TypeError, ValueError)):
#                 average(input_list)
#         else:
#             self.assertEqual(average(input_list), expected_output)


# For each test case, we use an if statement to check if the expected output is None. If it is, we use the assertRaises method with a tuple of exceptions to check that the function raises either a TypeError or ValueError. If it is not None, we use the assertEqual method to check that the function returns the correct average.

# ==================================================================================

# Exercise 5
# Suppose you have the function that sorts a list of strings alphabetically:


# def sort_strings(input_list):
#     if not isinstance(input_list, list):
#         raise TypeError("Input must be a list")
#     for item in input_list:
#         if not isinstance(item, str):
#             raise ValueError("All items must be strings")
#     return sorted(input_list)


# This function takes a list of strings as input, checks if the input is a list using the isinstance function, and raises a TypeError if it is not. It then checks if all items in the list are strings using a for loop, and raises a ValueError if any of them are not. It then sorts the list of strings alphabetically using the sorted function, and returns the sorted list.


# Use the parameterized library to write a parameterized test for the sort_strings() function.


# Test the sort_strings() function with the following different input lists:

# ["hello", "world"] -> ["hello", "world"]

# ["z", "a", "c"] -> ["a", "c", "z"]

# [] -> []

# ["hello", 123] -> None

# {"not": "a list"} -> None

# ["hello", None] -> None


# Tip: You should use the parameterized.expand decorator to create a parameterized test. The decorator takes a list of tuples, each containing the input list and the expected output. The expand function expands each tuple into a separate test case with the input list and expected output as arguments.

# Solution 5
# import unittest
# from parameterized import parameterized


# class TestSortStrings(unittest.TestCase):
#     @parameterized.expand(
#         [
#             (["hello", "world"], ["hello", "world"]),
#             (["z", "a", "c"], ["a", "c", "z"]),
#             ([], []),
#             (["hello", 123], None),
#             ({"not": "a list"}, None),
#             (["hello", None], None),
#         ]
#     )
#     def test_sort_strings(self, input_list, expected_output):
#         if expected_output is None:
#             with self.assertRaises((TypeError, ValueError)):
#                 sort_strings(input_list)
#         else:
#             self.assertEqual(sort_strings(input_list), expected_output)


# For each test case, we use an if statement to check if the expected output is None. If it is, we use the assertRaises method with a tuple of exceptions to check that the function raises either a TypeError or ValueError. If it is not None, we use the assertEqual method to check that the function returns the correct sorted list.
# ==================================================================================
if __name__ == '__main__':
    unittest.main(verbosity=2)
