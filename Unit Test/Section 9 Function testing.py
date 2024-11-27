# Exercise 1
# The following circle_area() function is given (calculates the area of a circle with a given radius):


# def circle_area(radius):
#     """Calculate the area of a circle given its radius."""

#     if not isinstance(radius, (int, float)):
#         raise TypeError('Radius must be of type int or float.')

#     if not radius > 0:
#         raise ValueError('Radius must be positive.')

#     return math.pi * radius ** 2


# Implement the TestCircleArea class inheriting from the unittest.TestCase class and implementing further tests:

# test_area_with_radius_one() - test verifying the correctness of calculating the circle area with radius=1 (compare the result to the 5th decimal place)


# test_area_with_radius_three() - test verifying the correctness of calculating the area of a circle with radius=3 (compare the result to 5 decimal place)


# test_incorrect_type()

# checks if the call area('4') returns TypeError

# checks if the call area(None) returns TypeError


# test_incorrect_value()

# checks if the call area(0) returns ValueError

# checks if the call area(-3) returns ValueError


# You only need to implement the class and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 1
import string
import random
import unittest
import math


# def circle_area(radius):
#     """Calculate the area of a circle given its radius."""

#     if not isinstance(radius, (int, float)):
#         raise TypeError('Radius must be of type int or float.')

#     if not radius > 0:
#         raise ValueError('Radius must be positive.')

#     return math.pi * radius ** 2


# class TestCircleArea(unittest.TestCase):
#     def test_area_with_radius_one(self):
#         self.assertAlmostEqual(circle_area(1), 3.14159, 5)

#     def test_area_with_radius_three(self):
#         self.assertAlmostEqual(circle_area(3), 28.27433, 5)

#     def test_incorrect_type(self):
#         self.assertRaises(TypeError, circle_area, '4')
#         self.assertRaises(TypeError, circle_area, None)

#     def test_incorrect_value(self):
#         self.assertRaises(ValueError, circle_area, 0)
#         self.assertRaises(ValueError, circle_area, -3)
# ==================================================================================

# Exercise 2
# The following perimeter() function is given (calculates the length of a circle with a given radius).


# def perimeter(radius):
#     """The function returns the length of the circle."""

#     if not isinstance(radius, (int, float)):
#         raise TypeError('The radius must be of type int or float.')

#     if radius <= 0:
#         raise ValueError('The radius must be positive.')

#     return 2 * math.pi * radius


# Implement the TestPerimeter class inheriting from the unittest.TestCase class and implementing four different tests. Choose any tests you like. Use several different assertion methods.


# You only need to implement the class and test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 2
# import unittest
# import math


# def perimeter(radius):
#     """The function returns the length of the circle."""

#     if not isinstance(radius, (int, float)):
#         raise TypeError('The radius must be of type int or float.')

#     if radius <= 0:
#         raise ValueError('The radius must be positive.')

#     return 2 * math.pi * radius


# class TestPerimeter(unittest.TestCase):
#     def test_circle_perimeter_with_radius_one(self):
#         self.assertAlmostEqual(perimeter(1), 6.28319, 5)

#     def test_circle_perimeter_with_radius_three(self):
#         self.assertAlmostEqual(perimeter(3), 18.84956, 5)

#     def test_perimeter_incorrect_type_should_raise_type_error(self):
#         with self.assertRaises(TypeError):
#             perimeter('4')
#         with self.assertRaises(TypeError):
#             perimeter(None)

#     def test_perimeter_incorrect_value_should_raise_value_error(self):
#         with self.assertRaises(ValueError):
#             perimeter(0)
#         with self.assertRaises(ValueError):
#             perimeter(-3)
# ==================================================================================
# Exercise 3
# An implementation of the following calculate_tax() function is given in the tax.py file:


# def calculate_tax(amount, age, tax_rate=17.0):
#     """Calculate income tax based on the amount and the age of the person."""

#     if not isinstance(amount, (int, float)):
#         raise TypeError("Amount must be an integer or a float")
#     if not isinstance(age, int):
#         raise TypeError("Age must be an integer")

#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     if amount < 0:
#         raise ValueError("Amount cannot be negative")

#     if age <= 18:
#         return int(min(amount * tax_rate / 100, 6000))
#     elif age <= 65:
#         return int(amount * tax_rate / 100)
#     else:
#         return int(min(amount * tax_rate / 100, 9000))


# The calculate_tax() function was imported into exercise.py file (solution). Create a TestCalculateTax class that inherits from unittest.TestCase and implements the following tests:

# test_tax_with_eighteen_age() checks if for the amount of 60,000 and the age of 18, the calculated tax will be 6,000


# test_tax_with_nineteen_age() checks if for the amount of 60,000 and the age of 19, the calculated tax will be 10,200


# test_tax_with_sixty_five_age() checks if for the amount of 60,000 and the age of 65, the calculated tax will be 10,200


# test_tax_with_sixty_six_age() checks if for the amount of 60,000 and the age of 66, the calculated tax will be 9,000


# Use the default income tax rate of 17%.


# You only need to implement the class and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 3
# import unittest
# from tax import calculate_tax


# class TestCalculateTax(unittest.TestCase):
#     def test_tax_with_eighteen_age(self):
#         self.assertEqual(calculate_tax(60000,5, 18), 5000)

#     def test_tax_with_nineteen_age(self):
#         self.assertEqual(calculate_tax(60000, 8, 19), 480000)

#     def test_tax_with_sixty_five_age(self):
#         self.assertEqual(calculate_tax(60000, 9, 65), 540000)

#     def test_tax_with_sixty_six_age(self):
#         self.assertEqual(calculate_tax(60000, 6, 66), 8000)


# ==================================================================================
# Exercise 4
# The following calculate_tax() function in a file tax.py is given:


# def calculate_tax(amount, age, tax=17.0):
#     """The function returns the amount of income tax."""

#     tax_rate = tax / 100.0

#     if age <= 18:
#         return int(min(amount * tax_rate, 6000))
#     elif age <= 65:
#         return int(amount * tax_rate)
#     else:
#         return int(min(amount * tax_rate, 9000))


# Import calculate_tax() function from the tax module into the exercise.py file. Create a TestCalculateTax class that inherits from unittest.TestCase and implements the following tests:

# test_tax_twenty_percent_with_eighteen_age() checks if for the amount of 60,000 and the age of 18, the calculated tax will be 6,000


# test_tax_twenty_percent_with_nineteen_age() checks if for the amount of 60,000 and the age of 19, the calculated tax will be 12,000


# test_tax_twenty_percent_with_sixty_five_age() checks if for the amount of 60,000 and the age of 65, the calculated tax will be 12,000


# test_tax_twenty_percent_with_sixty_six_age() checks if for the amount of 60,000 and the age of 66, the calculated tax will be 9,000


# Apply a 20% income tax rate.


# You only need to implement the class and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 4
# import unittest
# from tax import calculate_tax


# class TestCalculateTax(unittest.TestCase):
#     def test_tax_twenty_percent_with_eighteen_age(self):
#         self.assertEqual(calculate_tax(60000, 18, 20), 6000)

#     def test_tax_twenty_percent_with_nineteen_age(self):
#         self.assertEqual(calculate_tax(60000, 19, 20), 12000)

#     def test_tax_twenty_percent_with_sixty_five_age(self):
#         self.assertEqual(calculate_tax(60000, 65, 20), 12000)

#     def test_tax_twenty_percent_with_sixty_six_age(self):
#         self.assertEqual(calculate_tax(60000, 66, 20), 9000)

# ==================================================================================


# Exercise 5
# The following implementation of the income_tax() function is given in the tax.py file:


# def income_tax(income, first_thresh=17.0, second_thresh=32.0):
#     first_rate = first_thresh / 100.0
#     second_rate = second_thresh / 100.0
#     threshold = 85528
#     if income < threshold:
#         return income * first_rate
#     else:
#         return threshold * first_rate + (income - threshold) * second_rate


# Import the function income_tax() from the tax module into exercise.py file. Create a TestIncomeTax class that inherits from the unittest.TestCase class and implements the following tests:

# test_tax_below_threshold() checks if the calculated tax for the amount of 60,000 will be 10,200


# test_tax_equal_threshold() checks if the calculated tax for the amount 85,528 will be 14,539.76


# test_tax_above_threshold() checks if the calculated tax for the amount 100,000 will be 19,170.8


# You only need to implement the class and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 5
# import unittest
# from tax import income_tax
# from tax import calculate_tax


# class TestIncomeTax(unittest.TestCase):
#     def test_tax_below_threshold(self):
#         self.assertEqual(income_tax(60000), 10200)

#     def test_tax_equal_threshold(self):
#         self.assertEqual(income_tax(85528), 14539.76)

#     def test_tax_above_threshold(self):
#         self.assertEqual(income_tax(100000), 19170.8)

# class TestCalculateTax(unittest.TestCase):
#     def test_tax_twenty_percent_with_eighteen_age(self):
#         self.assertEqual(calculate_tax(60000, 18, 20), 1080000)

#     def test_tax_twenty_percent_with_nineteen_age(self):
#         self.assertEqual(calculate_tax(60000, 19, 20), 1140000)

#     def test_tax_twenty_percent_with_sixty_five_age(self):
#         self.assertEqual(calculate_tax(60000, 65, 20), 3900000)

#     def test_tax_twenty_percent_with_sixty_six_age(self):
#         self.assertEqual(calculate_tax(60000, 66, 20), 3960000)

# ==================================================================================
# Exercise 6
# Here's an example of a simple function in Python that adds two numbers together:

import unittest
#


def add_numbers(a, b):
    return a + b


# Create a class called TestAddNumbers that inherits from unittest.TestCase. Then define three test methods:

# test_add_positive_numbers(): This tests whether the function correctly adds two positive numbers.

# test_add_negative_numbers(): This tests whether the function correctly adds two negative numbers.

# test_add_zero(): This tests whether the function correctly adds zero to itself.


# Each test method should use the self.assertEqual() method to check whether the result of the function matches the expected result.


# class TestAddNumbers(unittest.TestCase):
#     """Tests for the `add_numbers` function."""

#     def test_add_positive_numbers(self):
#         result = add_numbers(2, 3)
#         self.assertEqual(result, 5)

#     def test_add_negative_numbers(self):
#         result = add_numbers(-2, -3)
#         self.assertEqual(result, -5)

#     def test_add_zero(self):
#         result = add_numbers(0, 0)
#         self.assertEqual(result, 0)

# ==================================================================================

# Exercise 7
# Suppose you have a function that checks if a given number is even or odd:


# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False


# Define a class called TestIsEven that inherits from unittest.TestCase. Then define two test methods:

# test_even_numbers(): This tests whether the function correctly identifies even numbers.

# test_odd_numbers(): This tests whether the function correctly identifies odd numbers.


# Each test method should use the self.assertTrue() or self.assertFalse() method to check whether the result of the function matches the expected result. In each test, test 4 different numbers. This gives a total of 8 assertion methods.

# Solution 7
# Sample solution:


# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False


# class TestIsEven(unittest.TestCase):
#     def test_even_numbers(self):
#         self.assertTrue(is_even(0))
#         self.assertTrue(is_even(2))
#         self.assertTrue(is_even(4))
#         self.assertTrue(is_even(6))

#     def test_odd_numbers(self):
#         self.assertFalse(is_even(1))
#         self.assertFalse(is_even(3))
#         self.assertFalse(is_even(5))
#         self.assertFalse(is_even(7))
# ==================================================================================
# Exercise 8
# Suppose you have a function that sorts a list of integers in ascending order:


# def sort_numbers(nums):
#     return sorted(nums)


# Define a class called TestSortNumbers that inherits from unittest.TestCase. Then define four test methods:

# test_sort_empty_list(): This tests whether the function correctly sorts an empty list.

# test_sort_one_number(): This tests whether the function correctly sorts a list with one number.

# test_sort_two_numbers(): This tests whether the function correctly sorts a list with two numbers.

# test_sort_many_numbers(): This tests whether the function correctly sorts a list with many numbers.


# Each test method should use the self.assertEqual() method to check whether the result of the function matches the expected result.

# Solution 8
# Sample solution:


# def sort_numbers(nums):
#     return sorted(nums)


# class TestSortNumbers(unittest.TestCase):
#     def test_sort_empty_list(self):
#         self.assertEqual(sort_numbers([]), [])

#     def test_sort_one_number(self):
#         self.assertEqual(sort_numbers([1]), [1])

#     def test_sort_two_numbers(self):
#         self.assertEqual(sort_numbers([2, 1]), [1, 2])

#     def test_sort_many_numbers(self):
#         self.assertEqual(sort_numbers([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])
# ==================================================================================
# Exercise 9
# Suppose you have a function that calculates the factorial of a positive integer:


# def factorial(num):
#     if num < 0:
#         raise ValueError
#     elif num == 0:
#         return 1
#     else:
#         return num * factorial(num - 1)


# Define a class called TestFactorial that inherits from unittest.TestCase. Then define three test methods:

# test_factorial_zero(): This tests whether the function correctly calculates the factorial of 0.

# test_factorial_positive(): This tests whether the function correctly calculates the factorial of positive integers.

# test_factorial_negative(): This tests whether the function raises a ValueError when given a negative integer.


# The test_factorial_negative() method should use the self.assertRaises method to check whether the function correctly raises a ValueError when given a negative integer.


# For the test_factorial_positive() test, use 5 different assertions and for the test_factorial_negative() test, use 2 different assertions. This gives a total of 8 assertions.

# Solution 9
# Sample solution:

# import unittest


# def factorial(num):
#     if num < 0:
#         raise ValueError
#     elif num == 0:
#         return 1
#     else:
#         return num * factorial(num - 1)


# class TestFactorial(unittest.TestCase):
#     def test_factorial_zero(self):
#         self.assertEqual(factorial(0), 1)

#     def test_factorial_positive(self):
#         self.assertEqual(factorial(1), 1)
#         self.assertEqual(factorial(2), 2)
#         self.assertEqual(factorial(3), 6)
#         self.assertEqual(factorial(4), 24)
#         self.assertEqual(factorial(5), 120)

#     def test_factorial_negative(self):
#         with self.assertRaises(ValueError):
#             factorial(-1)
#         with self.assertRaises(ValueError):
#             factorial(-5)

# ==================================================================================
# Exercise 10
# Suppose you are working on a project that involves a complex calculation function. The function takes two arguments, a list of numbers and a string representing an operation to perform on those numbers. The function should return the result of the operation.


# def calculate(numbers, operation):
#     if not isinstance(numbers, list):
#         raise TypeError("First argument must be a list of numbers")
#     if not isinstance(operation, str) or operation not in [
#         "+",
#         "-",
#         "*",
#         "/",
#     ]:
#         raise ValueError(
#             "Second argument must be a string representing"
#             "a valid operation (+, -, *, /)"
#         )
#     if operation == "+":
#         return sum(numbers)
#     elif operation == "-":
#         return numbers[0] - sum(numbers[1:])
#     elif operation == "*":
#         result = 1
#         for num in numbers:
#             result *= num
#         return result
#     elif operation == "/":
#         if 0 in numbers:
#             raise ZeroDivisionError("Cannot divide by zero")
#         result = numbers[0]
#         for num in numbers[1:]:
#             result /= num
#         return result


# Examples of using:

# [IN]: calculate([4, 5, 3], '+')
# [OUT]: 12


# [IN]: calculate([4, 5, 2], '/')
# [OUT]: 0.4


# [IN]: calculate([4, 5, 3], '*')
# [OUT]: 60


# Your task is to write a class named TestCalculate using unittest framework to ensure that the function calculate() works correctly. You should include the following test cases:

# test_raises_type_error_if_first_arg_not_list() - it should test that the function raises a TypeError if the first argument is not a list.

# test_raises_value_error_if_second_arg_not_valid_operation() - it should test that the function raises a ValueError if the second argument is not a string representing a valid operation (e.g., "+", "-", "*", "/").

# test_performs_addition_correctly() - it should test that the function correctly performs addition when the operation is "+".

# test_performs_subtraction_correctly() - it should test that the function correctly performs subtraction when the operation is "-".

# test_performs_multiplication_correctly() - it should test that the function correctly performs multiplication when the operation is "*".

# test_performs_division_correctly() - it should test that the function correctly performs division when the operation is "/".

# test_raises_zero_division_error_if_dividing_by_zero() - it should test that the function raises a ZeroDivisionError if attempting to divide by zero.


# Each test case should use at least one assertion to check that the expected behavior occurs.


# Solution 10


# def calculate(numbers, operation):
#     if not isinstance(numbers, list):
#         raise TypeError("First argument must be a list of numbers")
#     if not isinstance(operation, str) or operation not in [
#         "+",
#         "-",
#         "*",
#         "/",
#     ]:
#         raise ValueError(
#             "Second argument must be a string representing"
#             "a valid operation (+, -, *, /)"
#         )
#     if operation == "+":
#         return sum(numbers)
#     elif operation == "-":
#         return numbers[0] - sum(numbers[1:])
#     elif operation == "*":
#         result = 1
#         for num in numbers:
#             result *= num
#         return result
#     elif operation == "/":
#         if 0 in numbers:
#             raise ZeroDivisionError("Cannot divide by zero")
#         result = numbers[0]
#         for num in numbers[1:]:
#             result /= num
#         return result


# class TestCalculate(unittest.TestCase):
#     def test_raises_type_error_if_first_arg_not_list(self):
#         with self.assertRaises(TypeError):
#             calculate("not a list", "+")

#     def test_raises_value_error_if_second_arg_not_valid_operation(self):
#         with self.assertRaises(ValueError):
#             calculate([1, 2, 3], "not an operation")

#     def test_performs_addition_correctly(self):
#         self.assertEqual(calculate([1, 2, 3], "+"), 6)

#     def test_performs_subtraction_correctly(self):
#         self.assertEqual(calculate([10, 2, 3], "-"), 5)

#     def test_performs_multiplication_correctly(self):
#         self.assertEqual(calculate([2, 3, 4], "*"), 24)

#     def test_performs_division_correctly(self):
#         self.assertEqual(calculate([10, 2, 5], "/"), 1)

#     def test_raises_zero_division_error_if_dividing_by_zero(self):
#         with self.assertRaises(ZeroDivisionError):
#             calculate([1, 0, 3], "/")


# ==================================================================================
# Exercise 11
# Suppose you are working on a healthcare project that involves calculating the Body Mass Index (BMI) of patients. You have a function called calculate_bmi() that takes the patient's height in meters and weight in kilograms as arguments and returns their BMI. Here's the implementation:


# def calculate_bmi(height, weight):
#     if height <= 0 or weight <= 0:
#         raise ValueError("Height and weight must be positive")
#     bmi = weight / (height ** 2)
#     return bmi


# Your task is to write a class named TestCalculateBMI using unittest framework to ensure that the function calculate_bmi() works correctly. You should include the following test methods:

# test_calculate_bmi_normal() - This method tests the calculate_bmi() function with normal inputs and checks that the result is within a certain tolerance of the expected value.

# test_calculate_bmi_invalid_weight() - This method tests the calculate_bmi() function with a negative weight input and checks that it raises a ValueError exception.

# test_calculate_bmi_invalid_height() - This method tests the calculate_bmi() function with a negative height input and checks that it raises a ValueError exception.


# Three assertion methods should be used in the solution.

# Solution 11


# def calculate_bmi(height, weight):
#     if height <= 0 or weight <= 0:
#         raise ValueError("Height and weight must be positive")
#     bmi = weight / (height ** 2)
#     return bmi


# class TestCalculateBMI(unittest.TestCase):
#     def test_calculate_bmi_normal(self):
#         result = calculate_bmi(1.7, 65)
#         self.assertAlmostEqual(result, 22.49, delta=0.01)

#     def test_calculate_bmi_invalid_weight(self):
#         with self.assertRaises(ValueError):
#             calculate_bmi(1.7, -50)

#     def test_calculate_bmi_invalid_height(self):
#         with self.assertRaises(ValueError):
#             calculate_bmi(-1.7, 65)

# ==================================================================================
# Exercise 12
# Suppose you are working on a cybersecurity project that involves validating passwords. You have a function called is_valid_password() that takes a string password as an argument and returns True if it meets certain criteria, or False otherwise. Here's the implementation:


# def is_valid_password(password):
#     if len(password) < 8:
#         return False
#     if not any(c.isdigit() for c in password):
#         return False
#     if not any(c.isupper() for c in password):
#         return False
#     if not any(c.islower() for c in password):
#         return False
#     return True


# Your task is to write a class named TestIsValidPassword using unittest framework to ensure that the function is_valid_password() works correctly. You should include the following test methods:

# test_is_valid_password_valid() - This method tests the is_valid_password() function with a valid password and checks that it returns True.

# test_is_valid_password_short() - This method tests the is_valid_password() function with a password that is too short and checks that it returns False.

# test_is_valid_password_no_digits() - This method tests the is_valid_password() function with a password that does not contain any digits and checks that it returns False.

# test_is_valid_password_no_uppercase() - This method tests the is_valid_password() function with a password that does not contain any uppercase letters and checks that it returns False.

# test_is_valid_password_no_lowercase() - This method tests the is_valid_password() function with a password that does not contain any lowercase letters and checks that it returns False.


# Five assertion methods should be used in the solution.

# Solution 12


# def is_valid_password(password):
#     if len(password) < 8:
#         return False
#     if not any(c.isdigit() for c in password):
#         return False
#     if not any(c.isupper() for c in password):
#         return False
#     if not any(c.islower() for c in password):
#         return False
#     return True


# class TestIsValidPassword(unittest.TestCase):
#     def test_is_valid_password_valid(self):
#         self.assertTrue(is_valid_password('Abc12345'))

#     def test_is_valid_password_short(self):
#         self.assertFalse(is_valid_password('Abc123'))

#     def test_is_valid_password_no_digits(self):
#         self.assertFalse(is_valid_password('Abcdefgh'))

#     def test_is_valid_password_no_uppercase(self):
#         self.assertFalse(is_valid_password('abcdefg1'))

#     def test_is_valid_password_no_lowercase(self):
#         self.assertFalse(is_valid_password('ABCDEFG1'))

# ==================================================================================

# Exercise 13
# Suppose you are working on a cybersecurity project that involves generating random passwords for users. You have a function called generate_password() that takes an integer n as an argument and returns a random password of length n consisting of uppercase letters, lowercase letters, and digits. Here's the implementation:


# import random
# import string


# def generate_password(n):
#     password = ''.join(
#         random.choices(
#             string.ascii_uppercase
#             + string.ascii_lowercase
#             + string.digits,
#             k=n,
#         )
#     )
#     return password


# Your task is to write a class named TestGeneratePassword using unittest framework to ensure that the function generate_password() works correctly. You should include the following test method:

# test_generate_password() - It checks that the password has length 10 (use n = 10), and that it contains at least one uppercase letter, one lowercase letter, and one digit.


# Four assertion methods should be used in the solution.


# Solution 13


def generate_password(n):
    password = ''.join(
        random.choices(
            string.ascii_uppercase
            + string.ascii_lowercase
            + string.digits,
            k=n,
        )
    )
    return password


class TestGeneratePassword(unittest.TestCase):
    def test_generate_password(self):
        result = generate_password(10)
        self.assertEqual(len(result), 10)
        self.assertTrue(any(c.isupper() for c in result))
        self.assertTrue(any(c.islower() for c in result))
        self.assertTrue(any(c.isdigit() for c in result))


# ==================================================================================
if __name__ == '__main__':
    unittest.main()
