# Exercise 1
# Suppose you're tasked with creating a program that takes a list of numbers and returns the
# sum of all the even numbers in the list. You'll need to create a function called sum_even_numbers()
#  that takes a list of numbers as input and returns the sum of all the even numbers in the list.


# To ensure that your function works correctly, you want to use test-driven development (TDD) to
# write tests for the function before you write the function itself.
# You've written test cases that checks if the function correctly sums up all even numbers in a list:


# def test_sum_even_numbers():
#     assert sum_even_numbers([1, 2, 4, 5]) == 6, '[1, 2, 4, 5] failed'
#     assert sum_even_numbers([0, 3, 4, 6]) == 10, '[0, 2, 3, 4, 6] failed'
#     assert sum_even_numbers([2, 4, 6]) == 12, '[2, 4, 6] failed'
#     assert sum_even_numbers([1, 3, 5]) == 0, '[1, 3, 5] failed'
#     assert sum_even_numbers([]) == 0, '[] failed'


# Implement the sum_even_numbers() function so that it satisfies the test cases.


# Solution 1
def sum_even_numbers(numbers):
    even_numbers = [n for n in numbers if n % 2 == 0]
    return sum(even_numbers)


def test_sum_even_numbers():
    assert sum_even_numbers([1, 2, 4, 5]) == 6, '[1, 2, 4, 5] failed'
    assert sum_even_numbers([0, 3, 4, 6]) == 10, '[0, 2, 3, 4, 6] failed'
    assert sum_even_numbers([2, 4, 6]) == 12, '[2, 4, 6] failed'
    assert sum_even_numbers([1, 3, 5]) == 0, '[1, 3, 5] failed'
    assert sum_even_numbers([]) == 0, '[] failed'


test_sum_even_numbers()
# ==================================================================================

# Exercise 2
# Suppose you're tasked with creating a program that takes a string as input and returns the number of words in the string that start with a vowel (i.e. 'a', 'e', 'i', 'o', or 'u'). You need to create a function called cnt() that takes a string as input and returns the number of words in the string that start with a vowel.


# To ensure that your function works correctly, you want to use test-driven development (TDD) to write tests for the function before you write the function itself. You've written a test case that checks if the function correctly counts the number of words in a string that start with a vowel:


# def test_cnt():
#     assert cnt("dog cat egg") == 1, '"dog cat egg" failed'
#     assert cnt("Apple igloo pet") == 2, '"Apple igloo pet" failed'
#     assert cnt("file disk") == 0, '"file disk" failed'
#     assert cnt("xyz") == 0, '"xyz" failed'
#     assert cnt("") == 0, '"" failed'


# Implement the cnt() function so that it satisfies the test case.

# Solution 2
# def cnt(string):
#     words = string.split()
#     vowels = ["a", "e", "i", "o", "u"]
#     count = 0
#     for word in words:
#         if word[0].lower() in vowels:
#             count += 1
#     return count


# def test_cnt():
#     assert cnt("dog cat egg") == 1, '"dog cat egg" failed'
#     assert cnt("Apple igloo pet") == 2, '"Apple igloo pet" failed'
#     assert cnt("file disk") == 0, '"file disk" failed'
#     assert cnt("xyz") == 0, '"xyz" failed'
#     assert cnt("") == 0, '"" failed'

# ==================================================================================
# Exercise 3
# Suppose you're tasked with creating a program that generates a random password that meets certain criteria. The password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character. You'll need to create a function called generate_password() that generates a random password that meets these criteria.


# To ensure that your function works correctly, you want to use test-driven development (TDD) to write tests for the function before you write the function itself. You've written a test case that checks if the function correctly generates a random password that meets the specified criteria:


# def test_generate_password():
#     password = generate_password()
#     assert len(password) >= 8
#     assert any(c.islower() for c in password)
#     assert any(c.isupper() for c in password)
#     assert any(c.isdigit() for c in password)
#     assert any(c in string.punctuation for c in password)


# Implement the generate_password() function so that it satisfies the test case.


# Solution 3
# import string
# import random


# def generate_password():
#     while True:
#         password = "".join(
#             random.choices(
#                 string.ascii_letters
#                 + string.digits
#                 + string.punctuation,
#                 k=12,
#             )
#         )
#         if (
#             any(c.islower() for c in password)
#             and any(c.isupper() for c in password)
#             and any(c.isdigit() for c in password)
#             and any(c in string.punctuation for c in password)
#         ):
#             return password


# def test_generate_password():
#     password = generate_password()
#     assert len(password) >= 8, "1st failed"
#     assert any(c.islower() for c in password), "2nd failed"
#     assert any(c.isupper() for c in password), "3rd failed"
#     assert any(c.isdigit() for c in password), "4th failed"
#     assert any(c in string.punctuation for c in password), "5th failed"


# ==================================================================================

# Exercise 4
# As a Python developer, you need to implement a function that generates the first n numbers in the Fibonacci sequence, where n is a non-negative integer. You should use the unittest framework and test-driven development to develop and test your implementation.

# You've written tests for the function that check that the output is correct for various input values of n:


# import unittest
# from solution import fibonacci


# class TestFibonacci(unittest.TestCase):
#     def test_fibonacci(self):
#         self.assertEqual(fibonacci(0), [0])
#         self.assertEqual(fibonacci(1), [0, 1])
#         self.assertEqual(fibonacci(2), [0, 1, 1])
#         self.assertEqual(fibonacci(3), [0, 1, 1, 2])
#         self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3, 5])
#         self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8, 13])


# Next, implement the fibonacci() function using test-driven development in the solution.py file. You can start by writing a simple implementation that returns an empty list for any input value of n:


# def fibonacci(n):
#     return []


# Then, complete the implementation.


# Solution 4
# def fibonacci(n):
#     if n == 0:
#         return [0]
#     elif n == 1:
#         return [0, 1]
#     else:
#         fib = [0, 1]
#         for i in range(2, n + 1):
#             fib.append(fib[-1] + fib[-2])
#         return fib

# ==================================================================================
