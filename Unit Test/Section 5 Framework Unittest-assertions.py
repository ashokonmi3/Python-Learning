import unittest


# Exercise 1
# The following calculate_daily_return() function is given, which takes two arguments: open and close (open and close price of a financial instrument from a trading session). The function returns the value of the daily rate of return (in percent).


# def calculate_daily_return(
#     open_price: float, close_price: float
# ) -> float:
#     return round(((close_price / open_price) - 1) * 100, 2)


# Complete the implementation of the TestCalculateDailyReturn class by adding three test methods:

# test_positive_return()

# using the method assertEqual check if code
# calculate_daily_return(349.0, 360.0) returns the daily rate of return 3.15


# test_negative_return()

# using the method assertEqual check if code
# calculate_daily_return(349.0, 340.0) returns the daily rate of return -2.58


# test_zero_return()

# using the method assertEqual check if code
# calculate_daily_return(349.0, 349.0) returns the daily rate of return 0.0


# You only need to implement test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 1
import unittest


# def calculate_daily_return(
#     open_price: float, close_price: float
# ) -> float:
#     return round(((close_price / open_price) - 1) * 100, 2)


# class TestCalculateDailyReturn(unittest.TestCase):
#     def test_positive_return(self) -> None:
#         self.assertEqual(calculate_daily_return(349.0, 360.0), 3.15)

#     def test_negative_return(self) -> None:
#         self.assertEqual(calculate_daily_return(349.0, 340.0), -2.58)

#     def test_zero_return(self) -> None:
#         self.assertEqual(calculate_daily_return(349.0, 349.0), 0.0)
# ==================================================================================
# Exercise 2
# The following calculate_daily_return() function is given, which takes two arguments: open and close (open and close price of a financial instrument from a trading session). The function returns the value of the daily rate of return.


# def calculate_daily_return(
#     open_price: float, close_price: float
# ) -> float:
#     return round(((close_price / open_price) - 1) * 100, 7)


# Complete the implementation of the TestCalculateDailyReturn class by adding three test methods:

# test_positive_return()

# using the method assertAlmostEqual  check if code calculate_daily_return(349.0, 360.0) returns the appropriate value


# test_negative_return()

# using the method assertAlmostEqual check if code calculate_daily_return(349.0, 340.0) returns the appropriate value


# test_zero_return()

# using the method assertAlmostEqual check if code calculate_daily_return(349.0, 349.0) returns the appropriate value


# Note: Note how the assertAlmostEqual method works.


# You only need to implement test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.
# Solution 2

# =======================
# print(round(3.14159))  # Output: 3
# print(round(2.71828))  # Output: 3

# # # Rounding to a specific number of decimal places:
# print(round(3.14159, 2))  # Output: 3.14
# print(round(2.71828, 3))  # Output: 2.718

# # # Rounding with negative ndigits (rounding to tens, hundreds, etc.):
# print(round(1234.5678, -1))  # Output: 1230.0
# print(round(1234.5678, -2))  # Output: 1200.0
# =========================================


# def calculate_daily_return(
#     open_price: float, close_price: float
# ) -> float:
#     return round(((close_price / open_price) - 1) * 100, 7)


# class TestCalculateDailyReturn(unittest.TestCase):
#     def test_positive_return(self) -> None:
#         self.assertAlmostEqual(
#             calculate_daily_return(349, 360), 3.1518625
#         )

#     def test_negative_return(self) -> None:
#         self.assertAlmostEqual(
#             calculate_daily_return(349, 340), -2.5787966
#         )

#     def test_zero_return(self) -> None:
#         self.assertAlmostEqual(
#             calculate_daily_return(349.0, 349.0), 0.0
#         )

# ==================================================================================
# Exercise 3
# The following Doc class is given:


# class Doc:
#     def __init__(self, string: str) -> None:
#         self.string = string

#     def __repr__(self) -> str:
#         return f"Doc(string='{self.string}')"

#     def __lt__(self, other) -> bool:
#         return len(self.string) < len(other.string)

#     def __gt__(self, other) -> bool:
#         return len(self.string) > len(other.string)


# Using the unittest framework create a TestDoc class that inherits from the unittest.TestCase class that implements two test methods:

# test_less_than()

# checks if doc2 < doc1 - use the assertLess() method for this purpose

# checks if doc3 < doc1 - use the assertLess() method for this purpose


# test_greater_than()

# checks if doc1 > doc2 - use the assertGreater() method for this purpose

# checks if doc1 > doc3 - use the assertGreater() method for this purpose


# Where doc1, doc2, doc3 are instances of Doc class, respectively:


# doc1 = Doc('Technology')
# doc2 = Doc('Online')
# doc3 = Doc('Nature')


# You only need to implement the class and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.
# Solution 3
# import unittest


# class Doc:
#     def __init__(self, string: str) -> None:
#         self.string = string

#     def __repr__(self) -> str:
#         return f"Doc(string='{self.string}')"

#     def __lt__(self, other) -> bool:
#         return len(self.string) < len(other.string)

#     def __gt__(self, other) -> bool:
#         return len(self.string) > len(other.string)


# class TestDoc(unittest.TestCase):
#     def test_less_than(self) -> None:
#         doc1 = Doc('Technology')
#         doc2 = Doc('Online')
#         doc3 = Doc('Nature')
#         self.assertLess(doc2, doc1)
#         self.assertLess(doc3, doc1)

#     def test_greater_than(self) -> None:
#         doc1 = Doc('Technology')
#         doc2 = Doc('Online')
#         doc3 = Doc('Nature')
#         self.assertGreater(doc1, doc2)
#         self.assertGreater(doc1, doc3)

# ==================================================================================
# Exercise 4
# The following Doc class is given:


# class Doc:
#     def __init__(self, string: str) -> None:
#         self.string = string

#     def __repr__(self) -> str:
#         return f"Doc(string='{self.string}')"

#     def __eq__(self, other) -> bool:
#         return len(self.string) == len(other.string)

#     def __ne__(self, other) -> bool:
#         return len(self.string) != len(other.string)


# Using the unittest framework create a TestDoc class that inherits from the unittest.TestCase class that implements two test methods:

# test_equal()

# checks if doc1 == doc2 use the assertEqual() method for this purpose


# test_not_equal()

# checks if doc3 != doc1 use the assertNotEqual() method for this purpose

# checks if doc3 != doc2 use the assertNotEqual() method for this purpose


# Where doc1, doc2, doc3 are instances of Doc class, respectively:


# doc1 = Doc('Online')
# doc2 = Doc('Nature')
# doc3 = Doc('Technology')


# You only need to implement the class and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 4
import unittest


# class Doc:
#     def __init__(self, string: str) -> None:
#         self.string = string

#     def __repr__(self) -> str:
#         return f"Doc(string='{self.string}')"

#     def __eq__(self, other) -> bool:
#         return len(self.string) == len(other.string)

#     def __ne__(self, other) -> bool:
#         return len(self.string) != len(other.string)


# class TestDoc(unittest.TestCase):
#     def test_equal(self) -> None:
#         doc1 = Doc('Online')
#         doc2 = Doc('Nature')
#         self.assertEqual(doc1, doc2)

#     def test_not_equal(self) -> None:
#         doc1 = Doc('Online')
#         doc2 = Doc('Nature')
#         doc3 = Doc('Technology')
#         self.assertNotEqual(doc3, doc1)
#         self.assertNotEqual(doc3, doc2)

# ==================================================================================
# Exercise 5
# The implementation of the Employee class is given:


# class Employee:
#     """A simple class that describes an employee of the company."""

#     TAX_RATE = 0.17
#     BONUS_RATE = 0.10

#     def __init__(
#         self, first_name: str, last_name: str, salary: int
#     ) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary

#     def __str__(self) -> str:
#         return f'{self.first_name} {self.last_name}'

#     @property
#     def email(self) -> str:
#         return (
#             f'{self.first_name.lower()}.{self.last_name.lower()}'
#             '@mail.com'
#         )

#     @property
#     def tax(self) -> float:
#         return round(self.salary * self.TAX_RATE, 2)

#     def apply_bonus(self) -> None:
#         self.salary = int(self.salary * (1 + self.BONUS_RATE))


# Using the unittest framework create a TestEmployee class that inherits from the unittest.TestCase class that implements three test methods:

# test_has_email_attr()

# checks whether the Employee class has the attribute email, if the attribute is missing, return the message:


# 'The Employee class does not have an email attribute.'


# test_has_tax_attr()

# checks whether the Employee class has the attribute tax, if the attribute is missing, return the message:


# 'The Employee class does not have a tax attribute.'


# test_has_apply_bonus()

# checks whether the Employee class has the attribute apply_bonus, if the attribute is missing, return the message:


# 'The Employee class does not have an apply_bonus attribute.'


# Tip: Use the built-in function hasattr() and the assertTrue() assertion method.


# You only need to implement the class and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 5
# import unittest


# class Employee:
#     """A simple class that describes an employee of the company."""

#     TAX_RATE = 0.17
#     BONUS_RATE = 0.10

#     def __init__(
#         self, first_name: str, last_name: str, salary: int
#     ) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary

#     def __str__(self) -> str:
#         return f'{self.first_name} {self.last_name}'

#     @property
#     def email(self) -> str:
#         return (
#             f'{self.first_name.lower()}.{self.last_name.lower()}'
#             '@mail.com'
#         )

#     @property
#     def tax(self) -> float:
#         return round(self.salary * self.TAX_RATE, 2)

#     def apply_bonus(self) -> None:
#         self.salary = int(self.salary * (1 + self.BONUS_RATE))


# class TestEmployee(unittest.TestCase):
#     def test_has_email_attr(self) -> None:
#         msg = 'The Employee class does not have an email attribute.'
#         self.assertTrue(hasattr(Employee, 'email'), msg)

#     def test_has_tax_attr(self) -> None:
#         msg = 'The Employee class does not have a tax attribute.'
#         self.assertTrue(hasattr(Employee, 'tax'), msg)

#     def test_has_apply_bonus(self) -> None:
#         msg = 'The Employee class does not have an apply_bonus attr.'
#         self.assertTrue(hasattr(Employee, 'apply_bonus'), msg)

# print(emp1.email)
# print()
# emp1.tax= 100
# ==================================================================================
# Exercise 6
# The implementation of the Employee class is given:


# class Employee:
#     """A simple class that describes an employee of the company."""

#     TAX_RATE = 0.17
#     BONUS_RATE = 0.10

#     def __init__(
#         self, first_name: str, last_name: str, salary: int
#     ) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary

#     def __str__(self) -> str:
#         return f'{self.first_name} {self.last_name}'

#     @property
#     def email(self) -> str:
#         return (
#             f'{self.first_name.lower()}.{self.last_name.lower()}'
#             '@mail.com'
#         )

#     @property
#     def tax(self) -> float:
#         return round(self.salary * self.TAX_RATE, 2)

#     def apply_bonus(self) -> None:
#         self.salary = int(self.salary * (1 + self.BONUS_RATE))


# Using the unittest framework create a TestEmployee class that inherits from the unittest.TestCase class that implements two test methods:

# test_has_email_attr()

# checks whether the Employee class has the attribute email, if the attribute is missing, return the message:


# 'The Employee class does not have an email attribute.'


# test_has_email_property()

# checks if the email attribute of the Employee class is of the type property. Use the assertIsInstance() method for this purpose.


# You only need to implement the class and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


# Solution 6
# import unittest


# class Employee:
#     """A simple class that describes an employee of the company."""

#     TAX_RATE = 0.17
#     BONUS_RATE = 0.10

#     def __init__(
#         self, first_name: str, last_name: str, salary: int
#     ) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary

#     def __str__(self) -> str:
#         return f'{self.first_name} {self.last_name}'

#     @property
#     def email(self) -> str:
#         return (
#             f'{self.first_name.lower()}.{self.last_name.lower()}'
#             '@mail.com'
#         )

#     @property
#     def tax(self) -> float:
#         return round(self.salary * self.TAX_RATE, 2)

#     def apply_bonus(self) -> None:
#         self.salary = int(self.salary * (1 + self.BONUS_RATE))


# class TestEmployee(unittest.TestCase):
#     def test_has_email_attr(self) -> None:
#         msg = 'The Employee class does not have an email attribute.'
#         self.assertTrue(hasattr(Employee, 'email'), msg)

#     def test_has_email_property(self) -> None:
#         msg = 'The Employee class email attribute is not a property.'
#         self.assertIsInstance(
#             getattr(Employee, 'email'), property, msg
#         )

# ==================================================================================

# Exercise 7
# An implementation of the StringListOnly class is given:


# class StringListOnly(list):
#     def append(self, string: str) -> None:
#         if not isinstance(string, str):
#             raise TypeError(
#                 'Only object of type str can be added to the list.'
#             )
#         super().append(string)


# Only objects of type str can be added to the list of type StringListOnly using the append() method.


# Using the unittest framework create a TestStringListOnly class that inherits from the unittest.TestCase class that implements two test methods:

# test_append_string()

# checks if we can add an object of the str type to the StringListOnly instance using the append() method. Use the assertIn() method for this purpose.


# test_append_not_string_should_raise_error()

# checks if TypeError is raised when trying to add an instance of type list. To do this, use the assertRaises() method.

# checks if TypeError is raised when trying to add an instance of type bool. To do this, use the assertRaises() method.


# You only need to implement the class and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 7
# import unittest


# class StringListOnly(list):
#     def append(self, string: str) -> None:
#         if not isinstance(string, str):
#             raise TypeError(
#                 'Only object of type str can be added to the list.'
#             )
#         super().append(string)
#         print(list())


# class TestStringListOnly(unittest.TestCase):

#     def test_append_string(self) -> None:
#         slo = StringListOnly()
#         string = 'big_data'
#         slo.append(string)
#         print(slo)
#         self.assertIn(string, slo)

#     def test_append_not_string_should_raise_error(self) -> None:
#         slo = StringListOnly()
#         not_string_1 = ['big_data']
#         not_string_2 = True
#         with self.assertRaises(TypeError):
#             slo.append(not_string_1)
#         with self.assertRaises(TypeError):
#             slo.append(not_string_2)

# ==================================================================================
# Exercise 8
# An implementation of the StringListOnly class is given:


# class StringListOnly(list):
#     def append(self, string):
#         if not isinstance(string, str):
#             raise TypeError(
#                 'Only object of type str can be added to the list.'
#             )
#         super().append(string)


# Only objects of type str can be added to the list of type StringListOnly using the append() method.


# Using the unittest framework create a TestStringListOnly class that inherits from the unittest.TestCase class that implements the test method:

# test_slo_is_instance()

# checks if instance slo = StringListOnly() is an instance of the StringListOnly class. Use the assertIsInstance() method.

# checks if instance slo = StringListOnly() is an instance of the list class. Use the assertIsInstance() method.


# You only need to implement the class and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 8
# import unittest


# class StringListOnly(list):
#     def append(self, string: str) -> None:
#         if not isinstance(string, str):
#             raise TypeError(
#                 'Only object of type str can be added to the list.'
#             )
#         super().append(string)


# class TestStringListOnly(unittest.TestCase):
#     def test_slo_is_instance(self) -> None:
#         slo = StringListOnly()
#         self.assertIsInstance(slo, StringListOnly)
#         self.assertIsInstance(slo, list)

# ==================================================================================
# Exercise 9
# Suppose you have the Calculator class with the divide method:


# class Calculator:
#     def divide(self, dividend, divisor):
#         if divisor == 0:
#             raise ValueError("Cannot divide by zero")
#         return dividend / divisor


# Create the unit test class named TestCalculator and define the following test cases:

# test_divide_positive_numbers()

# test_divide_zero_by_positive_number()

# test_divide_negative_by_positive_number()

# test_divide_by_zero_should_raise_error()


# Use the setUp() and tearDown() methods to create an instance of the Calculator class only once and delete it after the tests have been executed.

# Solution 9
# import unittest


# class Calculator:
#     def divide(self, dividend: float, divisor: float) -> float:
#         if divisor == 0:
#             raise ValueError("Cannot divide by zero")
#         return dividend / divisor


# class TestCalculator(unittest.TestCase):
#     def setUp(self) -> None:
#         self.calculator = Calculator()
#         print("setUP")

#     def test_divide_positive_numbers(self) -> None:
#         print("test_divide_positive_numbers")
#         self.assertEqual(self.calculator.divide(10, 2), 5)

#     def test_divide_zero_by_positive_number(self) -> None:
#         print("test_divide_zero_by_positive_number")

#         self.assertEqual(self.calculator.divide(0, 5), 0)

#     def test_divide_negative_by_positive_number(self) -> None:
#         print("test_divide_negative_by_positive_number")

#         self.assertEqual(self.calculator.divide(-10, 2), -5)

#     def test_divide_by_zero_should_raise_error(self) -> None:
#         print("test_divide_by_zero_should_raise_error")

#         with self.assertRaises(ValueError):
#             self.calculator.divide(10, 0)

#     def tearDown(self) -> None:
#         print("TearDown")
#         del self.calculator

# ==================================================================================

# Exercise 10
# Suppose you have the function that reads the number of lines from a file:


# def count_lines(filename):
#     with open(filename, 'r') as f:
#         lines = f.readlines()
#         return len(lines)


# This function opens the file with the given filename, reads all the lines, and returns the number of lines in the file.


# Define a class called TestCountLines that inherits from unittest.TestCase. Then define two test methods:

# test_count_lines_of_existing_file(): The first test case checks that the count_lines() function returns the correct number of lines for an existing file named evaluate.py. It should have 21 lines.

# test_count_lines_of_non_existing_file(): The second test case checks that the count_lines() function raises a FileNotFoundError exception when given a non-existing file named non_existing_script.py.

# Solution 10
import unittest


def count_lines(filename: str) -> int:
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File {filename} not found") from e


class TestCountLines(unittest.TestCase):
    def test_count_lines_of_existing_file(self) -> None:
        self.assertEqual(count_lines('evaluate.py'), 21)

    def test_count_lines_of_non_existing_file(self) -> None:
        with self.assertRaises(FileNotFoundError):
            count_lines('non_existing_script.py')

# ==================================================================================
# Exercise 11
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


# Your task is to write test case to ensure that this function works properly. Write your test case using built-in unittest module. Define a class called TestCalculateGrade that inherits from unittest.TestCase and implement the following test method:

# test_valid_input() - this test case checks that calling calculate_grade() with valid input returns the expected output - you should use six assertion methods with different inputs

# Solution 11
# import unittest


def calculate_grade(scores):
    if not isinstance(scores, list):
        raise TypeError("Input must be a list")
    if not scores:
        raise ValueError("List cannot be empty")
    if not all(isinstance(score, (int, float)) for score in scores):
        raise TypeError("Elements of list must be numbers")
    if not all(0 <= score <= 100 for score in scores):
        raise ValueError("Elements of list must be between 0 and 100")
    return sum(scores) / len(scores)


# class TestCalculateGrade(unittest.TestCase):
#     def test_valid_input(self):
#         self.assertAlmostEqual(
#             calculate_grade([90, 80, 70, 60]), 75.0, places=2
#         )
#         self.assertAlmostEqual(
#             calculate_grade([100, 90, 80, 70]), 85.0, places=2
#         )
#         self.assertAlmostEqual(
#             calculate_grade([50, 60, 70, 80]), 65.0, places=2
#         )
#         self.assertAlmostEqual(
#             calculate_grade([85, 75, 95, 80, 70]), 81.0, places=2
#         )
#         self.assertAlmostEqual(
#             calculate_grade([60, 80, 75, 70]), 71.25, places=2
#         )
#         self.assertAlmostEqual(
#             calculate_grade([100, 90]), 95.0, places=2
#         )


# ==================================================================================
if __name__ == '__main__':
    unittest.main()
