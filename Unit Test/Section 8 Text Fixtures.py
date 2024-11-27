

# Exercise 1
# The following code is given:


import sys
import unittest


# class Container:

#     def __init__(self):
#         if sys.platform.startswith('win'):
#             self.code = 'XC-win'
#         else:
#             self.code = f'XC-{sys.platform}'


# class TestContainer(unittest.TestCase):

#     @unittest.skipUnless(
#         sys.platform.startswith('win'), 'Requires Windows.'
#     )
#     def test_requires_windows(self):
#         container = Container()
#         self.assertEqual(container.code, 'XC-win')

#     @unittest.skipUnless(
#         sys.platform.startswith('linux'), 'Requires Linux.'
#     )
#     def test_requires_linux(self):
#         container = Container()
#         self.assertEqual(container.code, 'XC-linux')


# Note that we use the same piece of code in each test:


# container = Container()


# Try to replace these two pieces of code by adding the setUpModule() function, which will create a Container instance named container at the level of the entire test module. The container instance should be reachable from within each test.


# During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 1
import sys
import unittest


# class Container:
#     def __init__(self):
#         if sys.platform.startswith('win'):
#             self.code = 'XC-win'
#         else:
#             self.code = f'XC-{sys.platform}'


# class TestContainer(unittest.TestCase):
#     @unittest.skipUnless(
#         sys.platform.startswith('win'), 'Requires Windows.'
#     )
#     def test_requires_windows(self):
#         self.assertEqual(container.code, 'XC-win')

#     @unittest.skipUnless(
#         sys.platform.startswith('linux'), 'Requires Linux.'
#     )
#     def test_requires_linux(self):
#         self.assertEqual(container.code, 'XC-linux')


# def setUpModule():
#     global container
#     container = Container()
# ==================================================================================
# Exercise 2
# The following code is given:


import sys
import unittest


# class Container:
#     def __init__(self):
#         if sys.platform.startswith('win'):
#             self.code = 'XC-win'
#         else:
#             self.code = f'XC-{sys.platform}'


# class TestContainer(unittest.TestCase):
#     @unittest.skipUnless(
#         sys.platform.startswith('win'), 'Requires Windows.'
#     )
#     def test_requires_windows(self):
#         self.assertEqual(container.code, 'XC-win')

#     @unittest.skipUnless(
#         sys.platform.startswith('linux'), 'Requires Linux.'
#     )
#     def test_requires_linux(self):
#         self.assertEqual(container.code, 'XC-linux')


# def setUpModule():
#     global container
#     container = Container()


# Add a function called tearDownModule() that will allow you to remove the container instance after testing is complete.


# During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 2
import sys
import unittest


# class Container:
#     def __init__(self):
#         if sys.platform.startswith('win'):
#             self.code = 'XC-win'
#         else:
#             self.code = f'XC-{sys.platform}'


# class TestContainer(unittest.TestCase):
#     @unittest.skipUnless(
#         sys.platform.startswith('win'), 'Requires Windows.'
#     )
#     def test_requires_windows(self):
#         self.assertEqual(container.code, 'XC-win')

#     @unittest.skipUnless(
#         sys.platform.startswith('linux'), 'Requires Linux.'
#     )
#     def test_requires_linux(self):
#         self.assertEqual(container.code, 'XC-linux')


# def setUpModule():
#     global container
#     container = Container()


# def tearDownModule():
#     global container
#     del container

# ==================================================================================
# Exercise 3
# The following code is given:


# import sys
# import unittest


# class Container:
#     def __init__(self):
#         if sys.platform.startswith('win'):
#             self.code = 'XC-win'
#         else:
#             self.code = f'XC-{sys.platform}'


# class TestContainer(unittest.TestCase):
#     @unittest.skipUnless(
#         sys.platform.startswith('win'), 'Requires Windows.'
#     )
#     def test_requires_windows(self):
#         container = Container()
#         self.assertEqual(container.code, 'XC-win')

#     @unittest.skipUnless(
#         sys.platform.startswith('linux'), 'Requires Linux.'
#     )
#     def test_requires_linux(self):
#         container = Container()
#         self.assertEqual(container.code, 'XC-linux')


# Note that we use the same piece of code in each test:


# container = Container()


# Try to override these two pieces of code by adding a class method called setUpClass() of TestContainer class, which will allow you to create a Container instance at the level of the entire test class (as an attribute of the TestContainer class) named container.


# During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


# Solution 3
import sys
import unittest


# class Container:
#     def __init__(self):
#         if sys.platform.startswith('win'):
#             self.code = 'XC-win'
#         else:
#             self.code = f'XC-{sys.platform}'


# class TestContainer(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.container = Container()

#     @unittest.skipUnless(
#         sys.platform.startswith('win'), 'Requires Windows.'
#     )
#     def test_requires_windows(self):
#         self.assertEqual(self.container.code, 'XC-win')

#     @unittest.skipUnless(
#         sys.platform.startswith('linux'), 'Requires Linux.'
#     )
#     def test_requires_linux(self):
#         self.assertEqual(self.container.code, 'XC-linux')
# ==================================================================================

# Exercise 4
# The following code is given:


# import sys
# import unittest


# class Container:
#     def __init__(self):
#         if sys.platform.startswith('win'):
#             self.code = 'XC-win'
#         else:
#             self.code = f'XC-{sys.platform}'


# class TestContainer(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.container = Container()

#     @unittest.skipUnless(
#         sys.platform.startswith('win'), 'Requires Windows.'
#     )
#     def test_requires_windows(self):
#         self.assertEqual(self.container.code, 'XC-win')

#     @unittest.skipUnless(
#         sys.platform.startswith('linux'), 'Requires Linux.'
#     )
#     def test_requires_linux(self):
#         self.assertEqual(self.container.code, 'XC-linux')


# Add a class method named tearDownClass() to remove the container attribute of TestContainer (after performing all tests in this class.)


# During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


# Solution 4
# import sys
# import unittest


# class Container:
#     def __init__(self):
#         if sys.platform.startswith('win'):
#             self.code = 'XC-win'
#         else:
#             self.code = f'XC-{sys.platform}'


# class TestContainer(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.container = Container()

#     @classmethod
#     def tearDownClass(cls):
#         del cls.container

#     @unittest.skipUnless(
#         sys.platform.startswith('win'), 'Requires Windows.'
#     )
#     def test_requires_windows(self):
#         self.assertEqual(self.container.code, 'XC-win')

#     @unittest.skipUnless(
#         sys.platform.startswith('linux'), 'Requires Linux.'
#     )
#     def test_requires_linux(self):
#         self.assertEqual(self.container.code, 'XC-linux')
# ==================================================================================
# Exercise 5
# The following code is given:


# import sys
# import unittest


# class Container:
#     def __init__(self, category):
#         self.category = category

#     def __repr__(self):
#         return f"Container(category='{self.category}')"


# class TestContainer(unittest.TestCase):
#     def test_init_method(self):
#         container = Container('plastic')
#         msg = (
#             'The container instance does not have a category '
#             'attribute.'
#         )
#         self.assertTrue(hasattr(container, 'category'), msg)
#         self.assertEqual(container.category, 'plastic')

#     def test_repr_method(self):
#         container = Container('plastic')
#         self.assertEqual(
#             repr(container), "Container(category='plastic')"
#         )


# Note that we use the same piece of code in each test:


# container = Container('plastic')


# Try to replace these two pieces of code by adding a method called setUp() of the TestContainer class, which will allow you to create an instance of the Container class at the level of each test (as an attribute of the TestContainer class) named container.


# During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 5
# import sys
# import unittest


# class Container:
#     def __init__(self, category):
#         self.category = category

#     def __repr__(self):
#         return f"Container(category='{self.category}')"


# class TestContainer(unittest.TestCase):
#     def setUp(self):
#         self.container = Container('plastic')

#     def test_init_method(self):
#         msg = (
#             'The container instance does not have a category '
#             'attribute.'
#         )
#         self.assertTrue(hasattr(self.container, 'category'), msg)
#         self.assertEqual(self.container.category, 'plastic')

#     def test_repr_method(self):
#         self.assertEqual(
#             repr(self.container), "Container(category='plastic')"
#         )

# ==================================================================================

# Exercise 6
# The following code is given:


# import sys
# import unittest


# class Container:
#     def __init__(self, category):
#         self.category = category

#     def __repr__(self):
#         return f"Container(category='{self.category}')"


# class TestContainer(unittest.TestCase):
#     def setUp(self):
#         self.container = Container('plastic')

#     def test_init_method(self):
#         msg = (
#             'The container instance does not have a category '
#             'attribute.'
#         )
#         self.assertTrue(hasattr(self.container, 'category'), msg)
#         self.assertEqual(self.container.category, 'plastic')

#     def test_repr_method(self):
#         self.assertEqual(
#             repr(self.container), "Container(category='plastic')"
#         )


# Add a method named tearDown() to remove the container attribute of TestContainer class after each test.


# During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 6
# import sys
# import unittest


# class Container:
#     def __init__(self, category):
#         self.category = category

#     def __repr__(self):
#         return f"Container(category='{self.category}')"


# class TestContainer(unittest.TestCase):
#     def setUp(self):
#         self.container = Container('plastic')

#     def tearDown(self):
#         del self.container

#     def test_init_method(self):
#         msg = (
#             'The container instance does not have a category '
#             'attribute.'
#         )
#         self.assertTrue(hasattr(self.container, 'category'), msg)
#         self.assertEqual(self.container.category, 'plastic')

#     def test_repr_method(self):
#         self.assertEqual(
#             repr(self.container), "Container(category='plastic')"
#         )
# ==================================================================================
# Exercise 7
# Suppose you have the Calculator class with the add and subtract methods:


# class Calculator:
#     def add(self, x, y):
#         return x + y

#     def subtract(self, x, y):
#         return x - y


# Write a unit test for a Calculator class that tests the addition and subtraction methods. Use the setUp() and tearDown() methods to create and destroy a new instance of the Calculator class for each test case.

# Solution 7
# Sample solution:

# import unittest


# class Calculator:
#     def add(self, x, y):
#         return x + y

#     def subtract(self, x, y):
#         return x - y


# class TestCalculator(unittest.TestCase):
#     def setUp(self):
#         self.calculator = Calculator()

#     def tearDown(self):
#         del self.calculator

#     def test_add(self):
#         result = self.calculator.add(2, 3)
#         self.assertEqual(result, 5)

#     def test_subtract(self):
#         result = self.calculator.subtract(3, 2)
#         self.assertEqual(result, 1)


# ==================================================================================
# Exercise 8
# Suppose you have the FileReader class with the read_file() method:


# class FileReader:
#     def read_file(self, filename):
#         with open(filename, 'r') as f:
#             return f.read()


# Create the unit test class and test the read_file() method. You should use the setUp() and tearDown() methods to create and destroy a new test file for each test case. Use the tempfile library to create a temporary file containing the text "Hello, world!".


# Solution 8
# import unittest
# import tempfile


# class FileReader:
#     def read_file(self, filename):
#         with open(filename, 'r') as f:
#             return f.read()


# class TestFileReader(unittest.TestCase):
#     def setUp(self):
#         # Create a new temporary file and write some data to it
#         self.file = tempfile.NamedTemporaryFile(mode='w', delete=False)
#         self.file.write("Hello, world!")
#         self.file.close()

#     def tearDown(self):
#         # Delete the temporary file
#         import os
#         os.unlink(self.file.name)

#     def test_read_file(self):
#         # Create a new instance of the FileReader class
#         reader = FileReader()

#         # Read the contents of the test file using the read_file method
#         result = reader.read_file(self.file.name)

#         # Check that the contents of the file match the expected value
#         self.assertEqual(result, "Hello, world!")
# ==================================================================================
