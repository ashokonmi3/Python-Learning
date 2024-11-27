# Exercise 1
# Using the unittest.mock library import the Mock class.
#  Then create an instance of this class with the name 'first_mock' (the name argument of the Mock class)
# and assign it to a variable named mock.

# Print the contents of the mock variable to the console.


# Expected result:


# <Mock name='first_mock' id='29821992'>


# Note: The id value may vary.

# Solution 1
from unittest.mock import Mock, patch
import random
from unittest.mock import patch
import unittest
from unittest.mock import Mock


# mock = Mock(name='first_mock')
# print(mock)
# ==================================================================================


# Exercise 2
# The following code snippet is given:


# import random
# from unittest.mock import Mock


# techs = ['python', 'sql', 'java', 'aws', 'c++']


# The random.choice() method selects a random element from the iterable object.

# Mock the random.choice() method from the random built-in module so that when this method is called,
# it returns 'aws' each time. Use the return_value argument of the Mock class for this purpose.
# Then call the random.choice() method and print the result to the console.


# Expected result:


# aws


# Solution 2

import random
from unittest.mock import Mock


# techs = ['python', 'sql', 'java', 'aws', 'c++']

# random.choice = Mock(return_value='aws')
# print(random.choice())


# # Alternative solution with patch():


# techs = ['python', 'sql', 'java', 'aws', 'c++']

# with patch('random.choice', return_value='aws'):
#     print(random.choice(techs))
# ==================================================================================
# Exercise 3
# The method random.choice() is mocked (from the random built-in module).
# Display the value of the call_count attribute of the mocked random.choice() method.
# Then call the random.choice() method once and display the value of the call_count attribute to the console again.


# Expected result:


# 0
# 1


# Solution 3
# Solution:

# import random
# from unittest.mock import Mock


# techs = ['python', 'sql', 'java', 'aws', 'c++']

# random.choice = Mock(return_value='aws')
# print(random.choice.call_count)
# random.choice()
# print(random.choice.call_count)


# # # Alternative solution with patch():


# techs = ['python', 'sql', 'java', 'aws', 'c++']

# with patch('random.choice', return_value='aws') as mock_choice:
#     print(mock_choice.call_count)
#     random.choice(techs)
#     print(mock_choice.call_count)
# ==================================================================================

# Exercise 4
# The implementation of the Programmer class is given.
# An instance of this class named programmer is also created. Using the unittest.mock library,
#  mock the random.choice() method so that it returns the name of the technology 'python' each time it is called.
#  Then call the get_random_tech() method on the programmer instance and print the returned value to the console.


# Expected result:


# python
# Solution 4
# Solution:


# class Programmer:
#     def __init__(self):
#         self.tech_names = []

#     def add_tech(self, tech_name):
#         name = tech_name.lower()
#         if name not in self.tech_names:
#             self.tech_names.append(name)
#         return self

#     def get_random_tech(self):
#         return random.choice(self.tech_names)


# programmer = Programmer()
# programmer.add_tech('python')
# programmer.add_tech('java')
# programmer.add_tech('sql')
# programmer.add_tech('aws')
# programmer.add_tech('django')

# random.choice = Mock(return_value='python')
# print(programmer.get_random_tech())


# Alternative solution with patch():

# import random
# from unittest.mock import patch


# class Programmer:
#     def __init__(self):
#         self.tech_names = []

#     def add_tech(self, tech_name):
#         name = tech_name.lower()
#         if name not in self.tech_names:
#             self.tech_names.append(name)
#         return self

#     def get_random_tech(self):
#         return random.choice(self.tech_names)


# programmer = Programmer()
# programmer.add_tech('python')
# programmer.add_tech('java')
# programmer.add_tech('sql')
# programmer.add_tech('aws')
# programmer.add_tech('django')

# with patch('random.choice', return_value='python'):
#     print(programmer.get_random_tech())
# ==================================================================================
# Exercise 5
# The implementation of the Programmer class is given. An instance of this class named programmer is also created.
# Using the patch() function from the unittest.mock library and the context manager, mock the random.choice() method
# so that it returns the technology name 'sql' every time it is called within the context manager.
# Then, within the context manager, call the get_random_tech() method on the programmer instance and print the
# returned value to the console.


# Expected value:


# sql


# Solution 5
# import random
# from unittest.mock import patch


# class Programmer:
#     def __init__(self):
#         self.tech_names = []

#     def add_tech(self, tech_name):
#         name = tech_name.lower()
#         if name not in self.tech_names:
#             self.tech_names.append(name)
#         return self

#     def get_random_tech(self):
#         return random.choice(self.tech_names)


# programmer = Programmer()
# programmer.add_tech('python')
# programmer.add_tech('java')
# programmer.add_tech('sql')
# programmer.add_tech('aws')
# programmer.add_tech('django')

# with patch('random.choice') as mock_random:
#     mock_random.return_value = 'sql'
#     print(programmer.get_random_tech())
# ==================================================================================

# Exercise 6
# The implementation of the Programmer class is given.
# An instance of this class named programmer is also created.
# At the module level implement a function called test_get_random_tech() that will return the result of calling
#  the get_random_tech() method on the programmer instance.
#  Then, using the @patch decorator from the unittest.mock library,
#  decorate the test_get_random_tech() function and mock the random.choice method so that each time the random.choice method is called inside test_get_random_tech(), the technology name 'c++' is returned. Then call the test_get_random_tech() function and print the result to the console.


# Expected result:


# c++


# Solution 6
import random
from unittest.mock import patch


# class Programmer:
#     def __init__(self):
#         self.tech_names = []

#     def add_tech(self, tech_name):
#         name = tech_name.lower()
#         if name not in self.tech_names:
#             self.tech_names.append(name)
#         return self

#     def get_random_tech(self):
#         return random.choice(self.tech_names)


# programmer = Programmer()
# programmer.add_tech('python')
# programmer.add_tech('sql')
# programmer.add_tech('java')
# programmer.add_tech('c++')
# programmer.add_tech('aws')


# @patch('random.choice')
# def test_get_random_tech(mock_random):
#     mock_random.return_value = 'c++'
#     return programmer.get_random_tech()


# print(test_get_random_tech())
# ==================================================================================
# Exercise 7
# The implementation of the get_code() function is given in the code_generator.py file.
# Implement a class named TestGetCode that inherits from unittest.
# TestCase and implements a test method named test_get_code_mock_should_return_30().
# The method is designed to test the get_code() function.
# Since the function works pseudo-randomly, we cannot predict its exact result every time.

# Using the @patch() decorator mock the random.randint method within test_get_code_mock_should_should_return_30()
# so that in the test method, calling this method returns 30.
# Then, assert the result of calling get_code() with the expected result 'CX-30'.

# You only need to define the class and the appropriate tests.
# During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


# Solution 7
import unittest
from unittest.mock import patch
# from code_generator import get_code

# import random


# def get_code():
#     return f'CX-{random.randint(1, 100)}'


# class TestGetCode(unittest.TestCase):
#     @patch('random.randint', return_value=30)
#     def test_get_code_mock_should_return_30(self, mocked_random):
#         actual = get_code()
#         expected = 'CX-30'
#         self.assertEqual(actual, expected)


# ==================================================================================
# Exercise 8
# The implementation of the get_message() function is given in message_generator.py file. Implement a class named TestGetMessage that inherits from unittest.TestCase and in this class implement a test method named test_get_message_with_friday(). The method is designed to test the get_message() function. This function uses the message_generator.get_today_name() function and works depending on when it is called.


# Using the @patch() decorator mock the message_generator.get_today_name function within test_get_message_with_friday(), so that the function call returns 'Friday' in the test method. Then, assert the result of calling get_message() with the expected result 'Hello Friday!'.


# You only need to define the class and the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


# Solution 8
# import unittest
# from unittest.mock import patch
# from message_generator import get_message


# class TestGetMessage(unittest.TestCase):
#     @patch('message_generator.get_today_name', return_value='Friday')
#     def test_get_message_with_friday(self, mock_day):
#         actual = get_message()
#         expected = 'Hello Friday!'
#         self.assertEqual(actual, expected)


# ==================================================================================
# Exercise 9
# The implementation of the get_message() function is given in message_generator.py file. Add a test method named test_get_message_with_monday() to the TestGetMessage class. The method is designed to test the get_message() function. This function uses the message_generator.get_today_name() function and works depending on when it is called.


# Using the @patch() decorator mock the message_generator.get_today_name function within test_get_message_with_monday(), so that in the test method this function returns the value 'Monday'. Then assert the result of calling the get_message() function with the expected result 'Hello Monday!'.


# You only need to define the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


# # Solution 9
# import unittest
# from unittest.mock import patch
# from message_generator import get_message


# class TestGetMessage(unittest.TestCase):
#     @patch('message_generator.get_today_name')
#     def test_get_message_with_friday(self, mock_day):
#         mock_day.return_value = 'Friday'
#         actual = get_message()
#         expected = 'Hello Friday!'
#         self.assertEqual(actual, expected)

#     @patch('message_generator.get_today_name')
#     def test_get_message_with_monday(self, mock_day):
#         mock_day.return_value = 'Monday'
#         actual = get_message()
#         expected = 'Hello Monday!'
#         self.assertEqual(actual, expected)

# ==================================================================================
# Exercise 10
# The implementation of the get_code_with_day() function in the code_generator.py file is given. Implement a class named TestGetCodeWithDay that inherits from unittest.TestCase with a test method named test_get_code_with_day_with_mocked_friday(). The purpose of this method is to test the get_code_with_day() function. Since this function works pseudo-randomly, we cannot predict the exact result every time.


# Using the @patch() decorator twice, mock the operation of the random.randint method and the code_generator.get_today_name function within test_get_code_with_day_with_mocked_friday() so that in the test method, calling:

# random.randint() returns 5

# code_generator.get_today_name() returns 'FRI'

# Then assert the result of calling get_code_with_day() with the expected result 'CX-5-FRI'.


# You only need to define the class and the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


# Solution 10
# import unittest
# from unittest.mock import patch
# from code_generator import get_code_with_day


# class TestGetCodeWithDay(unittest.TestCase):
#     @patch('code_generator.get_today_name')
#     @patch('random.randint')
#     def test_get_code_with_day_with_mocked_friday(
#         self, mock_int, mock_day
#     ):
#         mock_int.return_value = 5
#         mock_day.return_value = 'FRI'
#         actual = get_code_with_day()
#         expected = 'CX-5-FRI'
#         self.assertEqual(actual, expected)


# ==================================================================================
# Exercise 11
# The implementation of the get_code_with_day() function in the code_generator.py file is given. To the TestGetCodeWithDay class add the test method named test_get_code_with_day_with_mocked_monday(). The purpose of this method is to test the get_code_with_day() function. Since this function works pseudo-randomly, we cannot predict the exact result every time.


# Using the @patch() decorator twice mock the random.randint method and the code_generator.get_today_name function within test_get_code_with_day_with_mocked_monday() so that in the test method, calling:

# random.randint() returns 20

# code_generator.get_today_name() returns 'MON'

# Then assert the result of calling get_code_with_day() with the expected result 'CX-20-MON'.


# You only need to define the class and the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


# Solution 11
# import unittest
# from unittest.mock import patch
# from code_generator import get_code_with_day


# class TestGetCodeWithDay(unittest.TestCase):
#     @patch('code_generator.get_today_name')
#     @patch('random.randint')
#     def test_get_code_with_day_with_mocked_friday(
#         self, mock_int, mock_day
#     ):
#         mock_int.return_value = 30
#         mock_day.return_value = 'FRI'
#         actual = get_code_with_day()
#         expected = 'CX-30-FRI'
#         self.assertEqual(actual, expected)

#     @patch('code_generator.get_today_name')
#     @patch('random.randint')
#     def test_get_code_with_day_with_mocked_monday(
#         self, mock_int, mock_day
#     ):
#         mock_int.return_value = 20
#         mock_day.return_value = 'MON'
#         actual = get_code_with_day()
#         expected = 'CX-20-MON'
#         self.assertEqual(actual, expected)


# ==================================================================================
# Exercise 12
# The Programmer class is implemented in the employees.py file. Create a TestProgrammer class that inherits from the unittest.TestCase class and implements:

# a setUp() method that creates an instance of the Programmer class (assign this instance to the TestProgrammer class attribute named programmer). To this instance using the add_tech() method add the following technology names: 'python',  'sql',  'java',  'c++',  'aws'

# a test named test_get_random_tech_mocked_python() that tests the Programmer class's get_random_tech() method. Since the output of the method is nondeterministic, mock this method with the @patch.object() decorator so that its call returns the technology name 'python'.


# You only need to define the class and the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 12
# import unittest
# from unittest.mock import patch
# from employees import Programmer


# class TestProgrammer(unittest.TestCase):
#     def setUp(self):
#         self.programmer = Programmer()
#         self.programmer.add_tech('python') \
#             .add_tech('sql') \
#             .add_tech('java') \
#             .add_tech('c++') \
#             .add_tech('aws')

#     @patch.object(Programmer, 'get_random_tech')
#     def test_get_random_tech_mocked_python(self, mock_tech):
#         mock_tech.return_value = 'python'
#         result = self.programmer.get_random_tech()
#         self.assertEqual(result, 'python')


# ==================================================================================

# Exercise 13
# The Programmer class is implemented in the employees.py file. To the TestProgrammer class add:

# a test named test_get_random_tech_mocked_cpp(), which tests the Programmer class's get_random_tech() method. Since the result of the method is nondeterministic, mock this method with the @patch.object() decorator so that its call returns the technology name 'c ++'.


# You only need to define the appropriate test. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 13
# import unittest
# from unittest.mock import patch
# from employees import Programmer


# class TestProgrammer(unittest.TestCase):
#     def setUp(self):
#         self.programmer = Programmer()
#         self.programmer.add_tech('python') \
#             .add_tech('sql') \
#             .add_tech('java') \
#             .add_tech('c++') \
#             .add_tech('aws')

#     @patch.object(Programmer, 'get_random_tech')
#     def test_get_random_tech_mocked_python(self, mock_tech):
#         mock_tech.return_value = 'python'
#         actual = self.programmer.get_random_tech()
#         expected = 'python'
#         self.assertEqual(actual, expected)

#     @patch.object(Programmer, 'get_random_tech')
#     def test_get_random_tech_mocked_cpp(self, mock_tech):
#         mock_tech.return_value = 'c++'
#         actual = self.programmer.get_random_tech()
#         expected = 'c++'
#         self.assertEqual(actual, expected)

# ==================================================================================
# Exercise 14
# The Programmer class is implemented in the employees.py file. To the TestProgrammer class add:

# a test named test_display_random_tech_mocked() that tests the display_random_tech() method of the Programmer class. Since the result of the method is nondeterministic and depends on calling the get_random_tech() method, mock the get_random_tech() method with the @patch.object() decorator so that its call returns the technology name 'python'.


# You only need to define the appropriate test. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 14
# import unittest
# from unittest.mock import patch
# from employees import Programmer


# class TestProgrammer(unittest.TestCase):
#     def setUp(self):
#         self.programmer = Programmer()
#         self.programmer.add_tech('python') \
#             .add_tech('sql') \
#             .add_tech('java') \
#             .add_tech('c++') \
#             .add_tech('aws')

#     @patch.object(Programmer, 'get_random_tech')
#     def test_display_random_tech_mocked(self, mock_tech):
#         mock_tech.return_value = 'python'
#         result = self.programmer.display_random_tech()
#         self.assertEqual(result, 'Technology name: python')


# ==================================================================================
# Exercise 15
# The Programmer class is implemented in the employees.py file. To the TestProgrammer class add:

# a test named test_display_random_tech_mocked_cpp() that tests the display_random_tech() method of the Programmer class. Since the result of the method is nondeterministic and depends on calling the get_random_tech() method, mock the get_random_tech() method with the @patch.object() decorator so that its call returns the technology name 'c++'.


# You only need to define the appropriate test. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


# Solution 15
# import unittest
# from unittest.mock import patch
# from employees import Programmer


# class TestProgrammer(unittest.TestCase):
#     def setUp(self):
#         self.programmer = Programmer()
#         self.programmer.add_tech('python') \
#             .add_tech('sql') \
#             .add_tech('java') \
#             .add_tech('c++') \
#             .add_tech('aws')

#     @patch.object(Programmer, 'get_random_tech')
#     def test_display_random_tech_mocked_python(self, mock_tech):
#         mock_tech.return_value = 'python'
#         result = self.programmer.display_random_tech()
#         self.assertEqual(result, 'Technology name: python')

#     @patch.object(Programmer, 'get_random_tech')
#     def test_display_random_tech_mocked_cpp(self, mock_tech):
#         mock_tech.return_value = 'c++'
#         result = self.programmer.display_random_tech()
#         self.assertEqual(result, 'Technology name: c++')


# ==================================================================================
if __name__ == '__main__':
    unittest.main(verbosity=2)
