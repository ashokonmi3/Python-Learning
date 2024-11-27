# Assert the is_italy variable using the assert statement:
# countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
# is_italy = 'ITA' in countries

import unittest

# Method                   Checks that
# assertEqual(a, b)          a == b
# assertNotEqual(a, b)       a != b
# assertTrue(x)              bool(x) is True
# assertFalse(x)             bool(x) is False
# assertIs(a, b)             a is b
# assertIsNot(a, b)          a is not b
# assertIsNone(x)            x is None
# assertIsNotNone(x)         x is not None
# assertIn(a, b)             a in b
# assertNotIn(a, b)          a not in b
# assertIsInstance(a, b)     isinstance(a, b)
# assertNotIsInstance(a, b)  not isinstance(a, b)
# #


import unittest

# verify if the button of app works
# click on button --> opens a new webpage


# def appcheckbutton():
#     print()

# class TestAssertions(unittest.TestCase):

# def test_button(self):
#     print(" Launching the application")# real time you need to write python code to launch that application/website
#     buttonCheck= appcheckbutton('PLAY')
#     self.assertTrue(buttonCheck)
#     clockButton()
#     assertEqual(read the currentpage, exepected page)

#     def test_assertEqual(self):
#         self.assertEqual(5, 5)  # a == b

#     def test_assertNotEqual(self):
#         self.assertNotEqual(5, 6)  # a != b

#     def test_assertTrue(self):
#         self.assertTrue(True)  # bool(x) is True

#     def test_assertFalse(self):
#         self.assertFalse(False)  # bool(x) is False

#     def test_assertIs(self):
#         a = b = []
#         self.assertIs(a, b)  # a is b

#     def test_assertIsNot(self):
#         a = []
#         b = []
#         self.assertIsNot(a, b)  # a is not b

#     def test_assertIsNone(self):
#         x=None
#         self.assertIsNone(x)  # x is None

#     def test_assertIsNotNone(self):
#         self.assertIsNotNone(5)  # x is not None

#     def test_assertIn(self):
#         self.assertIn(3, [1, 2, 3])  # a in b

#     def test_assertNotIn(self):
#         self.assertNotIn(4, [1, 2, 3])  # a not in b

#     def test_assertIsInstance(self):
#         self.assertIsInstance(5, int)  # isinstance(a, b)

#     def test_assertNotIsInstance(self):
#         self.assertNotIsInstance(5, str)  # not isinstance(a, b)


# if __name__ == '__main__':
#     unittest.main()


# ==============================

# class TestCountries(unittest.TestCase):
#     def test_is_italy(self):
#         countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
#         is_italy = 'ITA' in countries
#         self.assertTrue(is_italy)


# if __name__ == '__main__':
#     unittest.main()
# ==========================


# class TestCountries(unittest.TestCase):
#     def test_is_canada(self):
#         countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
#         is_canada = 'CAN' in countries
#         # 'CAN' is not in the list, so is_canada should be False
#         self.assertTrue(is_canada)


# if __name__ == '__main__':
#     unittest.main()
# =============================
# The implementation of the max_min_diff() function is given:


# def max_min_diff(numbers):
#     """
#     Calculates the difference between the maximum and minimum number
#     in the given list.

#     :param numbers: A list of numbers.
#     :return: The difference between the maximum and minimum number
#     in the list.
#     """
#     return max(numbers) - min(numbers)


# Modify the implementation of the max_min_diff() function. By using the assert statement inside this function, add the ability to check the length of the numbers argument before returning the result. If the length of the numbers object is 0 raise the AssertionError with message:


# 'The input list cannot be empty.'


# Otherwise, it returns the correct result(the difference between the highest and lowest value for numbers).

# In case the module with the solution is run directly, call the max_min_diff() function passing an empty list.


# def max_min_diff(numbers):
#     """
#     Calculates the difference between the maximum and minimum number
#     in the given list.

#     :param numbers: A list of numbers.
#     :return: The difference between the maximum and minimum number
#     in the list.
#     :raises ValueError: If the list is empty.
#     """
#     assert len(numbers) != 0, 'The input list cannot be empty.'
#     return max(numbers) - min(numbers)


# if __name__ == '__main__':
#     max_min_diff([])

# [1, 2, 3, 4, 5]
# list is not empty
# list contains only numbers
# contains right digits


# def max_min_diff(numbers):
#     """
#     Calculates the difference between the maximum and minimum number
#     in the given list.

#     :param numbers: A list of numbers.
#     :return: The difference between the maximum and minimum number
#     in the list.
#     :raises AssertionError: If the list is empty.
#     """
#     assert len(numbers) != 0, 'The input list cannot be empty.'
#     return max(numbers) - min(numbers)


# class TestMaxMinDiff(unittest.TestCase):
#     def test_positive_numbers(self):
#         self.assertEqual(max_min_diff([1, 2, 3, 4, 5]), 4)

#     def test_negative_numbers(self):
#         self.assertEqual(max_min_diff([-10, -5, 0, 5, 10]), 20)

#     def test_mixed_numbers(self):
#         self.assertEqual(max_min_diff([3, -3, 3, -3, 3]), 6)

#     def test_single_element(self):
#         self.assertEqual(max_min_diff([42]), 0)

#     def test_empty_list(self):
#         with self.assertRaises(AssertionError):
#             max_min_diff([])


# if __name__ == '__main__':
#     unittest.main()
# ===============================
# def rectangle_area(width: int, height: int) -> int:
#     """
#     Calculates the area of a rectangle with given width and height.

#     :param width: The width of the rectangle.
#     :param height: The height of the rectangle.
#     :return: The area of the rectangle.
#     """
#     return width * height


# assert rectangle_area(4, 10) == 40
# assert rectangle_area(5, 6) == 50


# def rectangle_area(width: int, height: int) -> int:
#     """
#     Calculates the area of a rectangle with given width and height.

#     :param width: The width of the rectangle.
#     :param height: The height of the rectangle.
#     :return: The area of the rectangle.
#     """
#     return width * height


# class TestRectangleArea(unittest.TestCase):
#     def test_rectangle_area(self):
#         # Test with width 4 and height 10
#         self.assertEqual(rectangle_area(4, 10), 40)

#         # Test with width 5 and height 6
#         self.assertEqual(rectangle_area(5, 6), 30)


# if __name__ == '__main__':
#     unittest.main()

# ============================
# def rectangle_area(width: int, height: int) -> int:
#     """
#     Calculates the area of a rectangle with given width and height.

#     :param width: The width of the rectangle.
#     :param height: The height of the rectangle.
#     :return: The area of the rectangle.
#     :raises TypeError: If the width or height is not an integer.
#     :raises ValueError: If the width or height is not a positive integer.
#     """
#     if not isinstance(width, int) or not isinstance(height, int):
#         raise TypeError('The width and height must be integers.')
#     if width <= 0 or height <= 0:
#         raise ValueError(
#             'The width and height must be positive integers.'
#         )
#     return width * height


# assert rectangle_area('5', '4') == 20
# assert rectangle_area(-4, 5) == 20


# def rectangle_area(width: int, height: int) -> int:
#     """
#     Calculates the area of a rectangle with given width and height.

#     :param width: The width of the rectangle.
#     :param height: The height of the rectangle.
#     :return: The area of the rectangle.
#     :raises TypeError: If the width or height is not an integer.
#     :raises ValueError: If the width or height is not a positive integer.
#     """
#     if not isinstance(width, int) or not isinstance(height, int):
#         raise TypeError('The width and height must be integers.')
#     if width <= 0 or height <= 0:
#         raise ValueError('The width and height must be positive integers.')
#     return width * height


# class TestRectangleArea(unittest.TestCase):
#     def test_rectangle_area_valid(self):
#         # Test with valid inputs
#         self.assertEqual(rectangle_area(4, 10), 40)
#         self.assertEqual(rectangle_area(50, 60), 300)

#     def test_rectangle_area_invalid_type(self):
#         # Test with invalid type inputs
#         with self.assertRaises(TypeError):
#             rectangle_area('5', '4')
#         with self.assertRaises(TypeError):
#             rectangle_area(5, '4')

#     def test_rectangle_area_invalid_value(self):
#         # Test with invalid value inputs
#         with self.assertRaises(ValueError):
#             rectangle_area(-4, 5)
#         with self.assertRaises(ValueError):
#             rectangle_area(5, -4)
#         with self.assertRaises(ValueError):
#             rectangle_area(0, 5)
#         with self.assertRaises(ValueError):
#             rectangle_area(5, 0)


# if __name__ == '__main__':
#     unittest.main()


# ==============================
# The calculate_income_tax() function is given(no argument validation):
# Implement a function called test_calculate_income_tax() that asserts the following test cases:

# calculate_income_tax(60000, 0.15, 10) == 5000

# calculate_income_tax(60000, 0.15, 18) == 5000

# calculate_income_tax(60000, 0.15, 19) == 9000

# calculate_income_tax(60000, 0.15, 65) == 9000

# calculate_income_tax(60000, 0.15, 66) == 8000


# Then call test_calculate_income_tax() function.


# def calculate_income_tax(
#     amount: float, tax_rate: float, age: int
# ) -> int:
#     """
#     Calculates the income tax based on the given amount, tax rate,
#     and age.

#     :param amount: The amount of income.
#     :param tax_rate: The tax rate as a decimal.
#     :param age: The age of the taxpayer.
#     :return: The amount of income tax.
#     """
#     if age <= 18:
#         return int(min(amount * tax_rate, 5000))
#     elif age <= 65:
#         return int(amount * tax_rate)
#     else:
#         return int(min(amount * tax_rate, 8000))


# def test_calculate_income_tax():
#     assert calculate_income_tax(60000, 0.15, 10) == 5000
#     assert calculate_income_tax(60000, 0.15, 18) == 5000
#     assert calculate_income_tax(60000, 0.15, 19) == 9000
#     assert calculate_income_tax(60000, 0.15, 65) == 9000
#     assert calculate_income_tax(60000, 0.15, 66) == 8000


# if __name__ == '__main__':
#     test_calculate_income_tax()


# def calculate_income_tax(amount: float, tax_rate: float, age: int) -> int:
#     """
#     Calculates the income tax based on the given amount, tax rate,
#     and age.

#     :param amount: The amount of income.
#     :param tax_rate: The tax rate as a decimal.
#     :param age: The age of the taxpayer.
#     :return: The amount of income tax.
#     """
#     if age <= 18:
#         return int(min(amount * tax_rate, 5000))
#     elif age <= 65:
#         return int(amount * tax_rate)
#     else:
#         return int(min(amount * tax_rate, 8000))


# class TestCalculateIncomeTax(unittest.TestCase):
#     def test_under_18(self):
#         self.assertEqual(calculate_income_tax(60000, 0.15, 10), 5000)
#         self.assertEqual(calculate_income_tax(60000, 0.15, 18), 5000)

#     def test_between_19_and_65(self):
#         self.assertEqual(calculate_income_tax(60000, 0.15, 19), 9000)
#         self.assertEqual(calculate_income_tax(60000, 0.15, 65), 9000)

#     def test_above_65(self):
#         self.assertEqual(calculate_income_tax(60000, 0.15, 66), 8000)


# if __name__ == '__main__':
#     unittest.main()


# =============================


# def is_palindrome(string: str) -> bool:
#     """
#     Determines whether the given string is a palindrome.

#     :param string: The string to check.
#     :return: True if the string is a palindrome, False otherwise.
#     """
#     string = string.lower().replace(" ", "")
#     return string == string[::-1]


# class TestIsPalindrome(unittest.TestCase):
#     def test_racecar(self):
#         self.assertTrue(is_palindrome("racecar"))

#     def test_hello(self):
#         self.assertFalse(is_palindrome("hello"))

#     def test_panama(self):
#         self.assertTrue(is_palindrome("A man a plan a canal Panama"))

#     def test_numeric_palindrome(self):
#         self.assertTrue(is_palindrome("12321"))

#     def test_not_palindrome(self):
#         self.assertFalse(is_palindrome("not a palindrome"))


# if __name__ == '__main__':
#     unittest.main()
# # ===============================


def find_max_min(numbers: list) -> tuple:
    """
    Finds the maximum and minimum values in the given list.

    :param numbers: The list of numbers.
    :return: A tuple containing the maximum and minimum values.
    :raises ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("List is empty")

    if not isinstance(number,list):
        raise TypeError("Data is not list")

    maximum = minimum = numbers[0]

    for number in numbers[1:]:
        if number > maximum:
            maximum = number
        elif number < minimum:
            minimum = number

    return maximum, minimum


class TestFindMaxMin(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(find_max_min([1, 2, 3, 4, 5]), (5, 1))

    def test_unordered_list(self):
        self.assertEqual(find_max_min([10, 5, 7, 3, 8]), (10, 3))

    def test_negative_numbers(self):
        self.assertEqual(find_max_min([-1, -2, -3, -4, -5]), (-1, -5))

    def test_single_element_list(self):
        self.assertEqual(find_max_min([0]), (0, 0))

    def test_otherthany_list(self):
        with self.assertRaises(TypeError):
            find_max_min("python")
    
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_max_min([])


if __name__ == '__main__':
    unittest.main()


# ========================================
