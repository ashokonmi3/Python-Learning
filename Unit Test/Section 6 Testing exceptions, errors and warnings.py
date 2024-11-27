
import warnings
import unittest

# Exercise 1
# Suppose you have a function divide() that takes two arguments and returns the result of dividing the first argument by the second argument:


# def divide(x, y):
#     return x / y


# Your task is to write test case to ensure that this function raises the appropriate exception when given certain inputs. Write your test case using built-in unittest module. Define a class called TestDivide that inherits from unittest.TestCase and implement the following test method:

# test_divide_by_zero() - when the second argument is 0, the function should raise a ZeroDivisionError

# Solution 1


# def divide(x, y):
#     return x / y


# class TestDivide(unittest.TestCase):
#     def test_divide_by_zero(self):
#         with self.assertRaises(ZeroDivisionError):
#             divide(5, 0)
# ==================================================================================
# Exercise 2
# Suppose you have a function calculate_discount() that takes two arguments: a price and a discount rate, and returns the discounted price:


# def calculate_discount(price, discount_rate):
#     if not isinstance(price, (int, float)):
#         raise TypeError("Price must be a number")
#     if not isinstance(discount_rate, (int, float)):
#         raise TypeError("Discount rate must be a number")
#     if price < 0 or discount_rate < 0:
#         raise ValueError(
#             "Price and discount rate must be non-negative"
#         )
#     discount = price * discount_rate
#     return price - discount


# Your task is to write test cases to ensure that this function raises the appropriate exceptions when given certain inputs. Write your test cases using built-in unittest module. Define a class called TestCalculateDiscount that inherits from unittest.TestCase and implement the following test methods:

# test_non_number_price() - with a string argument for price and a float argument for discount_rate the function should rasie a TypeError

# test_negative_price() - with negative price the function should rasie a ValueError

# Solution 2
import unittest


# def calculate_discount(price, discount_rate):
#     if not isinstance(price, (int, float)):
#         raise TypeError("Price must be a number")
#     if not isinstance(discount_rate, (int, float)):
#         raise TypeError("Discount rate must be a number")
#     if price < 0 or discount_rate < 0:
#         raise ValueError(
#             "Price and discount rate must be non-negative"
#         )
#     discount = price * discount_rate
#     return price - discount


# class TestCalculateDiscount(unittest.TestCase):
#     def test_non_number_price(self):
#         with self.assertRaises(TypeError):
#             calculate_discount("five dollars", 0.1)

#     def test_negative_price(self):
#         with self.assertRaises(ValueError):
#             calculate_discount(-100, 0.1)


# ==================================================================================
# Exercise 3
# Suppose you have a function calculate_area() that takes the dimensions of a rectangle (length and width) and returns the area:


# def calculate_area(length, width):
#     if not isinstance(length, (int, float)):
#         raise TypeError("Length must be a number")
#     if not isinstance(width, (int, float)):
#         raise TypeError("Width must be a number")
#     if length <= 0 or width <= 0:
#         raise ValueError("Length and width must be positive")
#     return length * width


# Your task is to write test cases to ensure that this function raises the appropriate exceptions when given certain inputs. Write your test cases using built-in unittest module. Define a class called TestCalculateArea that inherits from unittest.TestCase and implement the following test methods:

# test_zero_values()

# test_negative_values()

# test_non_number_values()


# These test methods test the function for invalid inputs and check that the function raises the appropriate exceptions. Three assertion methods should be used in each test method.

# Solution 3
import unittest


# def calculate_area(length, width):
#     if not isinstance(length, (int, float)):
#         raise TypeError("Length must be a number")
#     if not isinstance(width, (int, float)):
#         raise TypeError("Width must be a number")
#     if length <= 0 or width <= 0:
#         raise ValueError("Length and width must be positive")
#     return length * width


# class TestCalculateArea(unittest.TestCase):
#     def test_zero_values(self):
#         with self.assertRaises(ValueError):
#             calculate_area(0, 4)
#         with self.assertRaises(ValueError):
#             calculate_area(2, 0)
#         with self.assertRaises(ValueError):
#             calculate_area(0, 0)

#     def test_negative_values(self):
#         with self.assertRaises(ValueError):
#             calculate_area(-2, 4)
#         with self.assertRaises(ValueError):
#             calculate_area(2, -4)
#         with self.assertRaises(ValueError):
#             calculate_area(-2, -4)

#     def test_non_number_values(self):
#         with self.assertRaises(TypeError):
#             calculate_area("two", 4)
#         with self.assertRaises(TypeError):
#             calculate_area(2, "four")
#         with self.assertRaises(TypeError):
#             calculate_area("two", "four")


# ==================================================================================

# Exercise 4
# Suppose you have a function find_longest_word() that takes a list of strings and returns the longest string:


# def find_longest_word(words):
#     if not isinstance(words, list):
#         raise TypeError("Input must be a list")
#     if not all(isinstance(word, str) for word in words):
#         raise TypeError("List must contain only strings")
#     if not words:
#         raise ValueError("List cannot be empty")
#     return max(words, key=len)


# Your task is to write test cases to ensure that this function raises the appropriate exceptions when given certain inputs. Write your test cases using built-in unittest module. Define a class called TestFindLongestWord that inherits from unittest.TestCase and implement the following test methods:

# test_empty_list() - when the input is an empty list, the function should raise a ValueError - you should use one assertion method

# test_non_string_elements() - when the input contains non-string elements, the function should raise a TypeError - you should use three assertion methods with different inputs


# These test methods test the function for invalid inputs and check that the function raises the appropriate exceptions. Four assertion methods should be used in the solution.

# Solution 4
# import unittest


# def find_longest_word(words):
#     if not isinstance(words, list):
#         raise TypeError("Input must be a list")
#     if not all(isinstance(word, str) for word in words):
#         raise TypeError("List must contain only strings")
#     if not words:
#         raise ValueError("List cannot be empty")
#     return max(words, key=len)


# class TestFindLongestWord(unittest.TestCase):
#     def test_empty_list(self):
#         with self.assertRaises(ValueError):
#             find_longest_word([])

#     def test_non_string_elements(self):
#         with self.assertRaises(TypeError):
#             find_longest_word(["apple", 5, "banana"])
#         with self.assertRaises(TypeError):
#             find_longest_word([True, False, None])
#         with self.assertRaises(TypeError):
#             find_longest_word(["hello", [1, 2, 3], "world"])
# ==================================================================================

# Exercise 5
# Suppose you have a function get_average_grade() that takes a dictionary of students and their grades and returns the average grade across all students:


# def get_average_grade(grades):
#     if not isinstance(grades, dict):
#         raise TypeError("Input must be a dictionary")
#     if not all(isinstance(key, str) for key in grades.keys()):
#         raise TypeError("Keys must be strings")
#     if not all(
#         isinstance(value, (int, float)) for value in grades.values()
#     ):
#         raise TypeError("Values must be numbers")
#     if not grades:
#         raise ValueError("Dictionary cannot be empty")
#     return sum(grades.values()) / len(grades)


# Your task is to write test cases to ensure that this function raises the appropriate exceptions when given certain inputs. Write your test cases using built-in unittest module. Define a class called TestGetAverageGrade that inherits from unittest.TestCase and implement the following test methods:

# test_empty_dict() - when the dictionary is empty, the function should raise a ValueError - you should use one assertion method

# test_non_string_keys() - when the dictionary keys are not strings, the function should raise a TypeError - you should use two assertion methods with different inputs

# test_non_numeric_values() - when the dictionary values are not numbers, the function should raise a TypeError - you should use two assertion methods with different inputs


# These test methods test the function for invalid inputs and check that the function raises the appropriate exceptions. Five assertion methods should be used in the solution.


# Solution 5
# import unittest


# def get_average_grade(grades):
#     if not isinstance(grades, dict):
#         raise TypeError("Input must be a dictionary")
#     if not all(isinstance(key, str) for key in grades.keys()):
#         raise TypeError("Keys must be strings")
#     if not all(
#         isinstance(value, (int, float)) for value in grades.values()
#     ):
#         raise TypeError("Values must be numbers")
#     if not grades:
#         raise ValueError("Dictionary cannot be empty")
#     return sum(grades.values()) / len(grades)


# class TestGetAverageGrade(unittest.TestCase):
#     def test_empty_dict(self):
#         with self.assertRaises(ValueError):
#             get_average_grade({})

#     def test_non_string_keys(self):
#         with self.assertRaises(TypeError):
#             get_average_grade({1: 90, "Bob": 80})
#         with self.assertRaises(TypeError):
#             get_average_grade({True: 90, "Bob": 80, "Charlie": 85})

#     def test_non_numeric_values(self):
#         with self.assertRaises(TypeError):
#             get_average_grade({"Alice": "A", "Bob": "B"})
#         with self.assertRaises(TypeError):
#             get_average_grade({"Alice": 90, "Bob": "B", "Charlie": 85})


# ==================================================================================
# Exercise 6
# Suppose you have a function calculate_shipping_cost() that takes the weight and destination of a package and returns the shipping cost:


# def calculate_shipping_cost(weight, destination):
#     if not isinstance(weight, (int, float)):
#         raise TypeError("Weight must be a number")
#     if weight <= 0:
#         raise ValueError("Weight must be greater than zero")
#     if not isinstance(destination, str):
#         raise TypeError("Destination must be a string")
#     if not destination:
#         raise ValueError("Destination cannot be empty")
#     if destination.lower() == "usa":
#         return 0
#     if destination.lower() == "canada":
#         return weight * 1.5
#     if destination.lower() == "mexico":
#         return weight * 2.0
#     return weight * 5.0


# Your task is to write test cases to ensure that this function raises the appropriate exceptions with specific error messages when given certain inputs. Write your test cases using built-in unittest module. Define a class called TestCalculateShippingCost that inherits from unittest.TestCase and implement the following test methods:

# test_non_numeric_weight() - when the weight is not a number, the function should raise a TypeError with the message "Weight must be a number"

# test_non_positive_weight() - when the weight is less than or equal to zero, the function should raise a ValueError with the message "Weight must be greater than zero"

# test_non_string_destination() - when the destination is not a string, the function should raise a TypeError with the message "Destination must be a string".

# test_empty_destination() - when the destination is an empty string, the function should raise a ValueError with the message "Destination cannot be empty"


# These test methods test the function for invalid inputs and check that the function raises the appropriate exceptions with specific error messages. Four assertion methods should be used in the solution.


# Solution 6
# import unittest


# def calculate_shipping_cost(weight, destination):
#     if not isinstance(weight, (int, float)):
#         raise TypeError("Weight must be a number")
#     if weight <= 0:
#         raise ValueError("Weight must be greater than zero")
#     if not isinstance(destination, str):
#         raise TypeError("Destination must be a string")
#     if not destination:
#         raise ValueError("Destination cannot be empty")
#     if destination.lower() == "usa":
#         return 0
#     if destination.lower() == "canada":
#         return weight * 1.5
#     if destination.lower() == "mexico":
#         return weight * 2.0
#     return weight * 5.0


# class TestCalculateShippingCost(unittest.TestCase):
#     def test_non_numeric_weight(self):
#         with self.assertRaisesRegex(
#             TypeError, "Weight must be a number"
#         ):
#             calculate_shipping_cost("5", "USA")

#     def test_non_positive_weight(self):
#         with self.assertRaisesRegex(
#             ValueError, "Weight must be greater than zero"
#         ):
#             calculate_shipping_cost(-100, "USA")

#     def test_non_string_destination(self):
#         with self.assertRaisesRegex(
#             TypeError, "Destination must be a string"
#         ):
#             calculate_shipping_cost(100, 50)

#     def test_empty_destination(self):
#         with self.assertRaisesRegex(
#             ValueError, "Destination cannot be empty"
#         ):
#             calculate_shipping_cost(100, "")

# ==================================================================================
# Exercise 7
# Suppose you have a function calculate_grade() that takes a list of student scores and returns the average grade:


# def calculate_grade(scores):
#     if not isinstance(scores, list):
#         raise TypeError("Input must be a list")
#     if not scores:
#         raise ValueError("List cannot be empty")
#     if not all(isinstance(score, (int, float)) for score in scores):
#         raise TypeError("Elements of list must be numbers")
#     if not all(0 <= score <= 100 for score in scores):
#         raise ValueError("Elements of list must be between 0 and 100")
#     return sum(scores) / len(scores)


# Your task is to write test cases to ensure that this function raises the appropriate exceptions with specific error messages when given certain inputs. Write your test cases using built-in unittest module. Define a class called TestCalculateGrade that inherits from unittest.TestCase and implement the following test methods:

# test_non_list_input() - when the input is not a list, the function should raise a TypeError with the message "Input must be a list".

# test_empty_list_input() - when the input list is empty, the function should raise a ValueError with the message "List cannot be empty".

# test_non_numeric_element() - when one or more elements of the list is not a number, the function should raise a TypeError with the message "Elements of list must be numbers".

# test_out_of_range_element() - when one or more elements of the list is not between 0 and 100, the function should raise a ValueError with the message "Elements of list must be between 0 and 100".


# These test methods test the function for invalid inputs and check that the function raises the appropriate exceptions with specific error messages. Four assertion methods should be used in the solution.


# Solution 7
# import unittest


# def calculate_grade(scores):
#     if not isinstance(scores, list):
#         raise TypeError("Input must be a list")
#     if not scores:
#         raise ValueError("List cannot be empty")
#     if not all(isinstance(score, (int, float)) for score in scores):
#         raise TypeError("Elements of list must be numbers")
#     if not all(0 <= score <= 100 for score in scores):
#         raise ValueError("Elements of list must be between 0 and 100")
#     return sum(scores) / len(scores)


# class TestCalculateGrade(unittest.TestCase):
#     def test_non_list_input(self):
#         with self.assertRaisesRegex(TypeError, "Input must be a list"):
#             calculate_grade(123)

#     def test_empty_list_input(self):
#         with self.assertRaisesRegex(ValueError, "List cannot be empty"):
#             calculate_grade([])

#     def test_non_numeric_element(self):
#         with self.assertRaisesRegex(
#             TypeError, "Elements of list must be numbers"
#         ):
#             calculate_grade([90, 80, "70", 60])

#     def test_out_of_range_element(self):
#         with self.assertRaisesRegex(
#             ValueError, "Elements of list must be between 0 and 100"
#         ):
#             calculate_grade([90, 80, 110, 60])
# ==================================================================================
# Exercise 8
# Suppose you have a function calculate_salary() that takes a list of hourly wages and hours worked, and returns the total salary:


# def calculate_salary(wages, hours):
#     if len(wages) != len(hours):
#         raise ValueError("Wages and hours lists must have the same length")
#     if not all(isinstance(wage, (int, float)) for wage in wages):
#         raise TypeError("Wages list must contain numbers")
#     if not all(isinstance(hour, (int, float)) for hour in hours):
#         raise TypeError("Hours list must contain numbers")
#     if not all(hour >= 0 for hour in hours):
#         raise ValueError("Hours must be non-negative")
#     if not all(wage >= 0 for wage in wages):
#         raise ValueError("Wages must be non-negative")
#     total_salary = sum([wages[i]*hours[i] for i in range(len(wages))])
#     if total_salary <= 0:
#         warnings.warn("Total salary is zero or negative")
#     return total_salary


# Your task is to write test cases to ensure that this function raises the appropriate exceptions and warnings when given certain inputs. Write your test cases using built-in unittest module. Define a class called TestCalculateSalary that inherits from unittest.TestCase and implement the following test methods:

# test_different_length_lists() - when the wages and hours lists have different lengths, the function should raise a ValueError with the message "Wages and hours lists must have the same length"

# test_non_numeric_wages() - when the wages list contains non-numeric elements, the function should raise a TypeError with the message "Wages list must contain numbers"

# test_non_numeric_hours() - when the hours list contains non-numeric elements, the function should raise a TypeError with the message "Hours list must contain numbers"

# test_negative_hours() - when the hours list contains negative values, the function should raise a ValueError with the message "Hours must be non-negative"

# test_negative_wages() - when the wages list contains negative values, the function should raise a ValueError with the message "Wages must be non-negative"

# test_zero_salary_warning() - when the total salary is zero or negative, the function should issue a UserWarning with the message "Total salary is zero or negative"


# These test methods test the function for invalid inputs and check that the function raises the appropriate exceptions with specific error messages. Six assertion methods should be used in the solution.

# Solution 8
import unittest
import warnings


# def calculate_salary(wages, hours):
#     if len(wages) != len(hours):
#         raise ValueError(
#             "Wages and hours lists must have the same length"
#         )
#     if not all(isinstance(wage, (int, float)) for wage in wages):
#         raise TypeError("Wages list must contain numbers")
#     if not all(isinstance(hour, (int, float)) for hour in hours):
#         raise TypeError("Hours list must contain numbers")
#     if not all(hour >= 0 for hour in hours):
#         raise ValueError("Hours must be non-negative")
#     if not all(wage >= 0 for wage in wages):
#         raise ValueError("Wages must be non-negative")
#     total_salary = sum([wages[i] * hours[i] for i in range(len(wages))])
#     if total_salary == 0:
#         warnings.warn("Total salary is zero or negative")
#     return total_salary


# class TestCalculateSalary(unittest.TestCase):
#     def test_different_length_lists(self):
#         with self.assertRaisesRegex(
#             ValueError,
#             "Wages and hours lists must have the same length",
#         ):
#             calculate_salary([10, 20, 30], [10, 20])

#     def test_non_numeric_wages(self):
#         with self.assertRaisesRegex(
#             TypeError, "Wages list must contain numbers"
#         ):
#             calculate_salary([10, 20, "30"], [10, 20, 30])

#     def test_non_numeric_hours(self):
#         with self.assertRaisesRegex(
#             TypeError, "Hours list must contain numbers"
#         ):
#             calculate_salary([10, 20, 30], [10, "20", 30])

#     def test_negative_hours(self):
#         with self.assertRaisesRegex(
#             ValueError, "Hours must be non-negative"
#         ):
#             calculate_salary([10, 20, 30], [10, -20, 30])

#     def test_negative_wages(self):
#         with self.assertRaisesRegex(
#             ValueError, "Wages must be non-negative"
#         ):
#             calculate_salary([10, -20, 30], [10, 20, 30])

#     def test_zero_salary_warning(self):
#         with self.assertWarns(
#             UserWarning, msg="Total salary is zero or negative"
#         ):
#             calculate_salary([10, 20, 30], [0, 0, 0])
# ==================================================================================

# Exercise 9
# Suppose you are working on a Python class User that represents a user in a system. The User class has an attribute called password that stores the user's password as a string. You want to make sure that if the password is too short (i.e., has fewer than 8 characters), a warning is raised when the User object is created.


# Here's the skeleton of the User class:


# import warnings


# class User:
#     def __init__(self, password):
#         self.password = password
#         if len(password) < 8:
#             warnings.warn("Password too short", category=Warning)


# Your task is to write a test case for this User class that uses the assertWarns() method to check that a warning is raised when the password is too short. Define a class called TestUser that inherits from unittest.TestCase and implement the following test method:

# test_short_password_warning() - checks that a warning is raised when the password is too short, and also check that the password has been created correctly - you should use two assertion methods


# Solution 9
import unittest


# class User:
#     def __init__(self, password):
#         self.password = password
#         if len(password) < 8:
#             warnings.warn("Password too short", category=Warning)


# class TestUser(unittest.TestCase):
#     def test_short_password_warning(self):
#         with self.assertWarns(Warning):
#             user = User("1234567")
#         self.assertEqual(user.password, "1234567")
# ==================================================================================

# Exercise 10
# Suppose you are working on a Python function called parse_data() that takes a string as input and tries to parse it as a dictionary using the json.loads() method. However, you realize that sometimes the input string may not be a valid JSON string, which would result in a ValueError being raised. You want to handle this situation by raising a warning instead of an error, and returning an empty dictionary as the result.


# Here's the skeleton of the parse_data() function:


# import json
# import warnings


# def parse_data(input_string):
#     try:
#         data = json.loads(input_string)
#     except ValueError:
#         warnings.warn("Invalid JSON string", category=Warning)
#         return {}
#     else:
#         return data


# Your task is to write a test case for this parse_data() function that uses the assertWarns() method to check that a warning is raised when the input string is not a valid JSON string. Define a class called TestParseData that inherits from unittest.TestCase and implement the following test method:

# test_invalid_json_warning() - checks that a warning is raised when the input string is not a valid JSON string, and also check if the empty dictionary was correctly returned - you should use two assertion methods

# Solution 10
# import json
# import unittest
# import warnings


# def parse_data(input_string):
#     try:
#         data = json.loads(input_string)
#     except ValueError:
#         warnings.warn("Invalid JSON string", category=Warning)
#         return {}
#     else:
#         return data

# class TestParseData(unittest.TestCase):
#     def test_invalid_json_warning(self):
#         with self.assertWarns(Warning):
#             result = parse_data('{"name": "Alice", "age": 30, }')
#         self.assertEqual(result, {})
# ==================================================================================
if __name__ == '__main__':
    unittest.main()
