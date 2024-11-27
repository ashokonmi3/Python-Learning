
# Automation tools
# selenium -- browser -- python
# Appium - mobile application testing - python
# Playwright - browser automation - python

# Jmeter - performance testing tool -- java

# POST MAN - used for REST API testing


# Exercise 1
# The implementation of the SimpleTaxCalculator class is given in the tax.py file. Import the SimpleTaxCalculator class from the tax module into the exercise.py file. Next, create a TestIncomeTax class that inherits from unittest.TestCase. Add the setUpClass() method to create an instance of the SimpleTaxCalculator class and assign it to the attribute named calc of the TestIncomeTax class.


# Test the income_tax() method of the SimpleTaxCalculator class. To do this implement the following test methods in the TestIncomeTax class:

# test_income_tax_below_threshold() checks if the calculated tax for income=60000 is equal to 10200


# test_income_tax_equal_threshold() checks if the calculated tax of income=85528 is equal to 14539.76


# test_income_tax_above_threshold() checks if the calculated tax of income=100000 is equal to 19170.8


# You only need to implement the class and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 1
from notebook import Note
from emp import Employee
import unittest
from tax import SimpleTaxCalculator


# class TestIncomeTax(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.calc = SimpleTaxCalculator()

#     def test_income_tax_below_threshold(self):
#         expected_tax = 10200
#         actual_tax = self.calc.income_tax(60000)
#         self.assertEqual(actual_tax, expected_tax)

#     def test_income_tax_equal_threshold(self):
#         expected_tax = 14539.76
#         actual_tax = self.calc.income_tax(85528)
#         self.assertEqual(actual_tax, expected_tax)

#     def test_income_tax_above_threshold(self):
#         expected_tax = 19170.8
#         actual_tax = self.calc.income_tax(100000)
#         self.assertEqual(actual_tax, expected_tax)
# ==================================================================================
# Exercise 2
# The implementation of the SimpleTaxCalculator class is given in the tax.py file. Add the TestVatTax class that inherits from the unittest.TestCase class to the exercise.py file. Also add the setUpClass() method to create an instance of the SimpleTaxCalculator class and assign it to an attribute named calc of the TestVatTax class.


# Test the vat_tax() method of the SimpleTaxCalculator class. To do this implement the following test methods in the TestVatTax class:

# test_vat_tax_with_zero_price()

# test_vat_tax_with_max_float_price() - you should use 'inf'

# test_vat_tax_with_string_input() -> it should raise TypeError


# You only need to implement the class and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 2
import unittest
from tax import SimpleTaxCalculator


# class TestIncomeTax(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.calc = SimpleTaxCalculator()

#     def test_income_below_threshold(self):
#         expected_tax = 10200
#         actual_tax = self.calc.income_tax(60000)
#         self.assertEqual(actual_tax, expected_tax)

#     def test_income_equal_threshold(self):
#         expected_tax = 14539.76
#         actual_tax = self.calc.income_tax(85528)
#         self.assertEqual(actual_tax, expected_tax)

#     def test_income_above_threshold(self):
#         expected_tax = 19170.8
#         actual_tax = self.calc.income_tax(100000)
#         self.assertEqual(actual_tax, expected_tax)


# class TestVatTax(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.calc = SimpleTaxCalculator()

#     def test_vat_tax_with_zero_price(self):
#         expected_tax = 0
#         actual_tax = self.calc.vat_tax(0)
#         self.assertEqual(actual_tax, expected_tax)

#     def test_vat_tax_with_max_float_price(self):
#         expected_tax = float('inf')
#         actual_tax = self.calc.vat_tax(float('inf'))
#         self.assertEqual(actual_tax, expected_tax)

#     def test_vat_tax_with_string_input(self):
#         with self.assertRaises(TypeError):
#             self.calc.vat_tax('price')


# ==================================================================================
# Exercise 3
# The implementation of the SimpleTaxCalculator class is given in the tax.py file. Add the TestCapitalGainsTax class that inherits from the unittest.TestCase class to the exercise.py file. Add the setUpClass() method to create a SimpleTaxCalculator instance and assign it to an attribute named calc of TestCapitalGainsTax.


# Test the capital_gains_tax() method of the SimpleTaxCalculator class. To do this implement the following test methods in the TestCapitalGainsTax class:

# test_capital_gains_tax_with_positive_profit() - for example 1000

# test_capital_gains_tax_with_zero_profit() - you should use 0

# test_capital_gains_tax_with_negative_profit() - for example -100

# test_capital_gains_tax_with_large_profit() - for example 1000000

# test_capital_gains_tax_with_float_profit() - for example 50.0

# test_capital_gains_tax_with_max_float_profit() - you should use 'inf'

# test_capital_gains_tax_with_string_profit() - for example '1000'

# test_capital_gains_tax_with_none_profit() - you should use None


# You only need to implement the class and the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 3
# import unittest
# from tax import SimpleTaxCalculator


# class TestCapitalGainsTax(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.calc = SimpleTaxCalculator()

#     def test_capital_gains_tax_with_positive_profit(self):
#         expected_tax = 190.0
#         actual_tax = self.calc.capital_gains_tax(1000)
#         self.assertEqual(actual_tax, expected_tax)

#     def test_capital_gains_tax_with_zero_profit(self):
#         expected_tax = 0.0
#         actual_tax = self.calc.capital_gains_tax(0)
#         self.assertEqual(actual_tax, expected_tax)

#     def test_capital_gains_tax_with_negative_profit(self):
#         expected_tax = 0.0
#         actual_tax = self.calc.capital_gains_tax(-1000)
#         self.assertEqual(actual_tax, expected_tax)

#     def test_capital_gains_tax_with_large_profit(self):
#         expected_tax = 190000.0
#         actual_tax = self.calc.capital_gains_tax(1000000)
#         self.assertEqual(actual_tax, expected_tax)

#     def test_capital_gains_tax_with_float_profit(self):
#         expected_tax = 9.5
#         actual_tax = self.calc.capital_gains_tax(50.0)
#         self.assertEqual(actual_tax, expected_tax)

#     def test_capital_gains_tax_with_max_float_profit(self):
#         expected_tax = float('inf')
#         actual_tax = self.calc.capital_gains_tax(float('inf'))
#         self.assertEqual(actual_tax, expected_tax)

#     def test_capital_gains_tax_with_string_profit(self):
#         with self.assertRaises(TypeError):
#             self.calc.capital_gains_tax('profit')

#     def test_capital_gains_tax_with_none_profit(self):
#         with self.assertRaises(TypeError):
#             self.calc.capital_gains_tax(None)


# ==================================================================================
# Exercise 4
# The implementation of the SimpleTaxCalculator class is given in the tax.py file. There are three test classes in exercise.py:

# IncomeTaxTest

# VatTaxTest

# CapitalGainsTaxTest


# Each of these classes implements a class method named setUpClass() that performs the same operation in each test class. Modify the solution to replace these three class methods with a single module-level function named setUpModule() that creates a SimpleTaxCalculator class instance named calc that is globally available.


# You only need to implement the appropriate function. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 4
# import unittest
# from tax import SimpleTaxCalculator


# class TestIncomeTax(unittest.TestCase):
#     def test_income_below_threshold(self):
#         self.assertEqual(calc.income_tax(60000), 10200)

#     def test_income_equal_threshold(self):
#         self.assertEqual(calc.income_tax(85528), 14539.76)

#     def test_income_above_threshold(self):
#         self.assertEqual(calc.income_tax(100000), 19170.8)


# class TestVatTax(unittest.TestCase):
#     def test_vat_tax_with_default(self):
#         self.assertEqual(calc.vat_tax(100), 23.0)


# class TestCapitalGainsTax(unittest.TestCase):
#     def test_positive_profit(self):
#         self.assertEqual(calc.capital_gains_tax(1000), 190.0)

#     def test_zero_profit(self):
#         self.assertEqual(calc.capital_gains_tax(0), 0.0)

#     def test_negative_profit(self):
#         self.assertEqual(calc.capital_gains_tax(-1000), 0.0)


# def setUpModule():
#     global calc
#     calc = SimpleTaxCalculator()

# ==================================================================================

# Exercise 5
# The implementation of the Employee class is given in the emp.py file. In the solution file (exercise.py) implement the TestEmployee class inheriting from unittest.TestCase. Add one test method to this class:

# test_email() which checks if the created employee (instance of the Employee class) with arguments:

# 'John'

# 'Smith'

# 40

# 80000

# has a valid email address: 'john.smith@mail.com'


# You only need to implement a class and a test method. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


# Solution 5
# import unittest
# from emp import Employee


# class TestEmployee(unittest.TestCase):
#     def setUp(self):
#         self.emp = Employee('John', 'Smith', 40, 80000)

#     def test_email(self):
#         self.assertEqual(self.emp.email, 'john.smith@mail.com')

# ==================================================================================

# Exercise 6
# The implementation of the Employee class is given in the emp.py file. In the solution file (exercise.py) add one test method to the TestEmployee class:

# test_email_after_changing_first_name() which checks if the created employee (instance of the Employee class) with arguments:

# 'John'

# 'Smith'

# 40

# 80000

# after changing the first name to 'Mike' has the correct email address: 'mike.smith@mail.com'


# You only need to implement the appropriate test method. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 6
# import unittest
# from emp import Employee


# class TestEmployee(unittest.TestCase):
#     def setUp(self):
#         self.emp = Employee('John', 'Smith', 40, 80000)

#     def test_email(self):
#         self.assertEqual(self.emp.email, 'john.smith@mail.com')

#     def test_email_after_changing_first_name(self):
#         self.emp.first_name = 'Mike'
#         self.assertEqual(self.emp.email, 'mike.smith@mail.com')
# ==================================================================================

# Exercise 7
# The implementation of the Employee class is given in the emp.py file. In the solution file (exercise.py) add one test method to the TestEmployee class:

# test_email_after_changing_last_name() which checks if the created employee (instance of the Employee class) with arguments:

# 'John'

# 'Smith'

# 40

# 80000

# after changing the name to 'Doe' has the correct value of the email address: 'john.doe@mail.com'


# You only need to implement the appropriate test method. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


# Solution 7
# import unittest
# from emp import Employee


# class TestEmployee(unittest.TestCase):
#     def setUp(self):
#         self.emp = Employee('John', 'Smith', 40, 80000)

#     def test_email(self):
#         self.assertEqual(self.emp.email, 'john.smith@mail.com')

#     def test_email_after_changing_first_name(self):
#         self.emp.first_name = 'Mike'
#         self.assertEqual(self.emp.email, 'mike.smith@mail.com')

#     def test_email_after_changing_last_name(self):
#         self.emp.last_name = 'Doe'
#         self.assertEqual(self.emp.email, 'john.doe@mail.com')
# ==================================================================================
# Exercise 8
# The implementation of the Employee class is given in the emp.py file. In the solution file (exercise.py) modify the TestEmployee class by adding the setUp() method that allows for each test to recreate an instance of the Employee class with arguments: 'John', 'Smith', 40, 80000 and assign it to the TestEmployee class attribute named emp.


# You only need to implement the appropriate function. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 8
# import unittest
# from emp import Employee


# class TestEmployee(unittest.TestCase):
#     def setUp(self):
#         self.emp = Employee('John', 'Smith', 40, 80000)

#     def test_email(self):
#         self.assertEqual(self.emp.email, 'john.smith@mail.com')

#     def test_email_after_changing_first_name(self):
#         self.emp.first_name = 'Mike'
#         self.assertEqual(self.emp.email, 'mike.smith@mail.com')

#     def test_email_after_changing_last_name(self):
#         self.emp.last_name = 'Doe'
#         self.assertEqual(self.emp.email, 'john.doe@mail.com')


# ==================================================================================
# Exercise 9
# The implementation of the Employee class is given in the emp.py file. The solution file (exercise.py) contains the implementation of the TestEmployee class. Add two test methods to this class:

# test_get_salary() which checks if the value of the employee's salary attribute is equal to 80000


# test_apply_bonus() which checks whether the execution of the apply_bonus() method of the Employee class correctly modifies the value of the salary attribute to 88000.


# You only need to implement the appropriate test methods. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 9
# import unittest
# from emp import Employee


# class TestEmployee(unittest.TestCase):
#     def setUp(self):
#         self.emp = Employee('John', 'Smith', 40, 80000)

#     def test_get_salary(self):
#         self.assertEqual(self.emp.salary, 80000)

#     def test_apply_bonus(self):
#         self.emp.apply_bonus()
#         self.assertEqual(self.emp.salary, 88000)

# ==================================================================================
# Exercise 10
# The implementation of the Note class is given in notebook.py file. In exercise.py complete the test_note_has_content_instance_attr() implementation to check if the Note instance has an instance attribute called content. Also pass a message in case an assertion error is raised, for example:


# 'A Note instance does not have a content attribute.'


# During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


# Solution 10
# import unittest
# from notebook import Note


# class TestNote(unittest.TestCase):
#     def setUp(self):
#         self.note = Note('Simple note.')

#     def test_note_has_content_instance_attr(self):
#         msg = 'A Note instance does not have a content attribute.'
#         self.assertTrue(hasattr(self.note, 'content'), msg)


# ==================================================================================

# Exercise 11
# The implementation of the Note class is given in notebook.py file. In exercise.py complete the test_note_has_category_class_attr() implementation to check if the Note instance has an instance attribute called CATEGORY. Also pass a message in case an assertion error is raised, for example:


# 'The Note class does not have a CATEGORY attribute.'


# During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 11
# import unittest


# class TestNote(unittest.TestCase):
#     def test_note_has_category_class_attr(self):
#         msg = 'The Note class does not have a CATEGORY attribute.'
#         self.assertTrue(hasattr(Note, 'CATEGORY'), msg)

# ==================================================================================
# Exercise 12
# The implementation of the Note class is given in notebook.py file. In exercise.py complete implementation of the test_search_notes_method() to test the Notebook class's search_notes() method. Consider how to write the assertion correctly. Using the search_notes() method, check if the created notes contain the word 'data' and compare with the expected result:


# ['Big Data', 'Data Science']


# During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 12
# # import unittest
# from notebook import Notebook


# class TestNotebook(unittest.TestCase):
#     def setUp(self):
#         self.notebook = Notebook()
#         self.notebook.add_note('Big Data')
#         self.notebook.add_note('Data Science')
#         self.notebook.add_note('Machine Learning')

#     def test_search_notes_method(self):
#         actual = self.notebook.search_notes('data')
#         expected = ['Big Data', 'Data Science']
#         self.assertEqual(actual, expected)


# ==================================================================================
# Exercise 13
# The Employee class is implemented in employees.py file. In the exercise.py file complete the test_employee_has_email_property(), which checks if the Employee class has an attribute named email as a property attribute. Do it in two steps:

# Assert that the Employee class has an attribute named email - use the assertTrue() assertion method and the hasattr() built-in function.

# Assert whether the Employee class attribute named email is an instance of the built-in property class or not - use the assertIsInstance() assertion method


# You only need to complete the test. During the verification of the solution, the test is run and in case of any errors, the test report will be printed to the console.

# Solution 13
# import unittest
# from employees import Employee


# class TestEmployee(unittest.TestCase):
#     def test_employee_has_email_property(self):
#         self.assertTrue(hasattr(Employee, 'email'))
#         self.assertIsInstance(Employee.email, property)

# ==================================================================================
# Exercise 14
# The implementation of the Product class in the products.py file is given. In exercise.py, complete the test_product_has_private_generate_id_method() implementation, which checks if the Product class has a callable attribute called _generate_id.

# Do it in two steps:

# Assert that the Product class has an attribute named _generate_id - use the assertTrue() assertion method and the hasattr() built-in function.

# Assert that the Product class attribute _generate_id is callable - use the assertTrue() assertion method and the callable() built-in function.


# You only need to complete the test. During the verification of the solution, the test is run and in case of any errors, the test report will be printed to the console.

# Solution 14
# import unittest
# from products import Product


# class TestProduct(unittest.TestCase):
#     def test_product_has_private_generate_id_method(self):
#         self.assertTrue(hasattr(Product, '_generate_id'))
#         self.assertTrue(callable(Product._generate_id))


# ==================================================================================

# Exercise 15
# Suppose you have a class called Calculator that performs basic arithmetic operations:


# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         if b == 0:
#             raise ValueError('division by zero')
#         return a / b


# Define a class called TestCalculator that inherits from unittest.TestCase. Then define four test methods:

# setUp(): This method is called before each test method, and creates an instance of the Calculator class that will be used for testing.

# test_add(): This tests whether the add method of the Calculator class correctly adds two numbers.

# test_subtract(): This tests whether the subtract method of the Calculator class correctly subtracts two numbers.

# test_multiply(): This tests whether the multiply method of the Calculator class correctly multiplies two numbers.

# test_divide(): This tests whether the divide method of the Calculator class correctly divides two numbers, and raises a ValueError when the second argument is zero.


# Each test method should use the self.assertEqual() method to check whether the result of the method call matches the expected result, and the self.assertRaises() method to check whether the method correctly raises a ValueError when needed. In test_divide() implement two assertions. This gives a total of 5 assertions.

# Solution 15
# Sample solution:

# import unittest


# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         if b == 0:
#             raise ValueError('division by zero')
#         return a / b


# class TestCalculator(unittest.TestCase):
#     def setUp(self):
#         self.calculator = Calculator()

#     def test_add(self):
#         result = self.calculator.add(2, 3)
#         self.assertEqual(result, 5)

#     def test_subtract(self):
#         result = self.calculator.subtract(5, 3)
#         self.assertEqual(result, 2)

#     def test_multiply(self):
#         result = self.calculator.multiply(2, 3)
#         self.assertEqual(result, 6)

#     def test_divide(self):
#         result = self.calculator.divide(6, 3)
#         self.assertEqual(result, 2)
#         with self.assertRaises(ValueError):
#             self.calculator.divide(6, 0)

# ==================================================================================

# Exercise 16
# Suppose you have the ShoppingCart class with the add_item() and remove_item() methods:


# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)

#     def remove_item(self, item):
#         self.items.remove(item)


# Create the unit test class named TestShoppingCart and define the test cases. In the test_add_remove_item() method tests the add_item() and remove_item() methods of the ShoppingCart class by creating a new instance of the class, calling the add_item() and remove_item() methods with different items, and checking that the items are added or removed from the items list using the assertIn(), assertNotIn(), and assertEqual() methods. You should use five assertion methods.

# Solution 16
# Sample solution:

import unittest


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)


class TestShoppingCart(unittest.TestCase):
    def test_add_remove_item(self):
        cart = ShoppingCart()
        cart.add_item("apple")
        self.assertIn("apple", cart.items)

        cart.add_item("banana")
        self.assertIn("apple", cart.items)
        self.assertIn("banana", cart.items)

        cart.remove_item("apple")
        self.assertNotIn("apple", cart.items)

        cart.remove_item("banana")
        self.assertEqual(len(cart.items), 0)


# ==================================================================================

# Exercise 17
# Suppose you have the StringProcessor class with the reverse_words() method:


# class StringProcessor:
#     def reverse_words(self, string):
#         words = string.split()
#         reversed_words = [word[::-1] for word in words]
#         return " ".join(reversed_words)


# Create the unit test class named TestStringProcessor and define the test cases. In the test_reverse_words() method tests the reverse_words() method of the StringProcessor class by creating a new instance of the class, calling the reverse_words() method with three different strings, and checking that the return value matches the expected result using the assertEqual() method. You should use three assertion methods.

# Solution 17
# import unittest


# class StringProcessor:
#     def reverse_words(self, string):
#         words = string.split()
#         reversed_words = [word[::-1] for word in words]
#         return " ".join(reversed_words)


# class TestStringProcessor(unittest.TestCase):
#     def test_reverse_words(self):
#         processor = StringProcessor()
#         self.assertEqual(
#             processor.reverse_words("hello world"), "olleh dlrow"
#         )
#         self.assertEqual(
#             processor.reverse_words("Python is fun"), "nohtyP si nuf"
#         )
#         self.assertEqual(
#             processor.reverse_words("reverse   spaces"), "esrever secaps"
#         )
# ==================================================================================

# Exercise 18
# Suppose you have a class called Person that represents a person's name, age, and gender. Your task is to write a set of unit tests for this class using the unittest framework.


# Here's the implementation of the Person class (see person.py file):


# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def __str__(self):
#         return f"{self.name} ({self.age}, {self.gender})"


# Create the unit test class named TestPerson and define the following test methods:

# test_person_attributes() - which checks the attributes of a person instance

# test_person_str_method() - which checks the Person class's __str__() method


# Prepare two different instances of the Person class in the test fixture setUp() method. You should use a total of eight assertion methods.

# Solution 18
# from person import Person


# class TestPerson(unittest.TestCase):
#     def setUp(self):
#         self.person1 = Person('Alice', 30, 'Female')
#         self.person2 = Person('Bob', 25, 'Male')

#     def test_person_attributes(self):
#         self.assertEqual(self.person1.name, 'Alice')
#         self.assertEqual(self.person1.age, 30)
#         self.assertEqual(self.person1.gender, 'Female')

#         self.assertEqual(self.person2.name, 'Bob')
#         self.assertEqual(self.person2.age, 25)
#         self.assertEqual(self.person2.gender, 'Male')

#     def test_person_str_method(self):
#         self.assertEqual(str(self.person1), 'Alice (30, Female)')
#         self.assertEqual(str(self.person2), 'Bob (25, Male)')
# ==================================================================================
# Exercise 19
# Suppose you have a class named ShoppingCart that represents a shopping cart and a class named Item that represents an item. Your task is to write a set of unit tests for this class using the unittest framework.


# Here's the implementation of the Item and ShoppingCart classes:


# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def get_price(self):
#         return self.price


# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)

#     def remove_item(self, item):
#         self.items.remove(item)

#     def get_total_price(self):
#         return sum(item.get_price() for item in self.items)


# Create the unit test class named TestShoppingCart and prepare a ShoppingCart object and two Item objects (item1 and item2) in the setUp() method. Then, define the following test methods:

# test_add_item() - This method should test the add_item() method of the ShoppingCart class. Add two items to the cart using the add_item() method, and verify that each item is in the cart, and that the number of items in the cart is correct. - You should use four assertion methods.

# test_remove_item() - This method should test the remove_item() method of the ShoppingCart class. Removes item1 from the cart using the remove_item() method, and verifies that item1 is not in the cart, and that the number of items in the cart is correct. - You should use two assertion methods.

# test_get_total_price() - This method should test the get_total_price() method of the ShoppingCart class. Call the get_total_price() method and verify that the total price of the items in the cart is correct. - You should use one assertion method.


# You should use a total of seven assertion methods.

# Solution 19
# import unittest
# from shopping_cart import Item, ShoppingCart


# class TestShoppingCart(unittest.TestCase):
#     def setUp(self):
#         self.cart = ShoppingCart()
#         self.item1 = Item('Book', 15)
#         self.item2 = Item('Shoes', 50)

#     def test_add_item(self):
#         self.cart.add_item(self.item1)
#         self.assertIn(self.item1, self.cart.items)
#         self.assertEqual(len(self.cart.items), 1)

#         self.cart.add_item(self.item2)
#         self.assertIn(self.item2, self.cart.items)
#         self.assertEqual(len(self.cart.items), 2)

#     def test_remove_item(self):
#         self.cart.add_item(self.item1)
#         self.cart.add_item(self.item2)
#         self.cart.remove_item(self.item1)
#         self.assertNotIn(self.item1, self.cart.items)
#         self.assertEqual(len(self.cart.items), 1)

#     def test_get_total_price(self):
#         self.cart.add_item(self.item1)
#         self.cart.add_item(self.item2)
#         self.assertEqual(self.cart.get_total_price(), 65)


# ==================================================================================

# Exercise 20
# Suppose you have a class called LinkedList that represents a singly linked list with methods to add and remove nodes, and traverse the list. Your task is to write a set of unit tests for this class using the unittest framework.


# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def add_node(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def remove_node(self, data):
#         current_node = self.head
#         previous_node = None

#         while current_node is not None:
#             if current_node.data == data:
#                 if previous_node is not None:
#                     previous_node.next = current_node.next
#                 else:
#                     self.head = current_node.next
#                 return True
#             previous_node = current_node
#             current_node = current_node.next

#         return False

#     def traverse_list(self):
#         current_node = self.head
#         while current_node is not None:
#             print(current_node.data)
#             current_node = current_node.next


# Create the unit test class named TestLinkedList and create a LinkedList object in the setUp() method. Then, define the following test methods:

# test_add_node() - This method should test the add_node() method of the LinkedList class. Add nodes to the list using the add_node() method, and verify that the head node is updated correctly using assertEqual(). - You should use two assertion methods.

# test_remove_node() - This method should test the remove_node() method of the LinkedList class. Add nodes to the list using the add_node() method. Then, remove a node from the list using the remove_node() method and verify that the node was removed correctly by calling assertEqual() with the expected and actual values. It also should test the case where the method is called with a non-existent node and verify that the method returns False. - You should use three assertion methods.

# test_traverse_list() - This method should test the traverse_list() method of the LinkedList class. Add nodes to the list using the add_node() method. Then, call the traverse_list() method and verify that the method prints the expected output by calling assertEqual() with the expected and actual values. Note that the expected output is not returned by the method, so we need to use the print() function inside the assertEqual() statement. - You should use one assertion methods.


# You should use a total of six assertion methods.


# Solution 20
# import unittest
# from linked_list import LinkedList


# class TestLinkedList(unittest.TestCase):
#     def setUp(self):
#         self.linked_list = LinkedList()

#     def test_add_node(self):
#         self.linked_list.add_node(1)
#         self.assertEqual(self.linked_list.head.data, 1)

#         self.linked_list.add_node(2)
#         self.assertEqual(self.linked_list.head.data, 2)

#     def test_remove_node(self):
#         self.linked_list.add_node(1)
#         self.linked_list.add_node(2)
#         self.linked_list.add_node(3)

#         self.assertEqual(self.linked_list.remove_node(2), True)
#         self.assertEqual(self.linked_list.head.next.data, 1)

#         self.assertEqual(self.linked_list.remove_node(4), False)

#     def test_traverse_list(self):
#         self.linked_list.add_node(1)
#         self.linked_list.add_node(2)
#         self.linked_list.add_node(3)

#         self.assertEqual(
#             self.linked_list.traverse_list(), print('3\n2\n1')
#         )

# ==================================================================================
# Exercise 21
# Suppose you have a class called BMI that represents a person's body mass index with methods to calculate the BMI and determine if it is in a healthy range. Your task is to write a set of unit tests for this class using the unittest framework.


# Here's how you can structure the code:


# class BMI:
#     def __init__(self, weight, height):
#         self.weight = weight
#         self.height = height

#     def calculate_bmi(self):
#         return self.weight / (self.height ** 2)

#     def is_healthy(self):
#         bmi = self.calculate_bmi()
#         if bmi < 18.5:
#             return 'underweight'
#         elif bmi >= 18.5 and bmi <= 24.9:
#             return 'healthy'
#         elif bmi >= 25 and bmi <= 29.9:
#             return 'overweight'
#         else:
#             return 'obese'


# Create the unit test class named TestBMI and create a BMI object with weight 70 kg and height 1.8 m in the setUp() method. Then, define the following test methods:

# test_calculate_bmi() - This test method tests the calculate_bmi() method of the BMI class. Calculate the BMI using the calculate_bmi() method and verify that the BMI was calculated correctly by calling assertAlmostEqual() with the expected and actual values and a tolerance of one decimal place. - You should use one assertion method.

# test_is_healthy() - This test method tests the is_healthy() method of the BMI class. Verify that the BMI is in a healthy range by calling assertEqual() with the expected and actual values. Then, create additional BMI objects with different weights and heights and verifies that the is_healthy() method returns the correct label for each BMI range by calling assertEqual() with the expected and actual values. - You should use four assertion methods.


# You should use a total of five assertion methods.

# Solution 21
# import unittest
# from bmi import BMI


# class TestBMI(unittest.TestCase):
#     def setUp(self):
#         self.bmi = BMI(70, 1.8)

#     def test_calculate_bmi(self):
#         self.assertAlmostEqual(
#             self.bmi.calculate_bmi(), 21.6, places=1
#         )

#     def test_is_healthy(self):
#         self.assertEqual(self.bmi.is_healthy(), 'healthy')

#         self.bmi = BMI(45, 1.6)
#         self.assertEqual(self.bmi.is_healthy(), 'underweight')

#         self.bmi = BMI(85, 1.8)
#         self.assertEqual(self.bmi.is_healthy(), 'overweight')

#         self.bmi = BMI(110, 1.8)
#         self.assertEqual(self.bmi.is_healthy(), 'obese')


# ==================================================================================

# Exercise 22
# Suppose you have a class called SecuritySystem (see security_system.py file and other files) that represents a security system with attributes such as cameras, sensors, and alarms, and methods to arm and disarm the system, as well as notify authorities in case of a breach. Your task is to write a set of unit tests for this class using the unittest framework.


# Create the unit test class named TestSecuritySystem and in the setUp() method create a SecuritySystem object using Camera, Sensor, and Alarm objects as arguments.


# Then, define the following test methods:

# test_arm() - It tests the arm() method of the SecuritySystem class. Call the arm() method of the SecuritySystem object and verify that the armed attribute is set to True. - You should use one assertion method.

# test_disarm() - It tests the disarm() method of the SecuritySystem class. Set the armed attribute of the SecuritySystem object to True, call the disarm() method, and verify that the armed attribute is set to False. - You should use one assertion method.

# test_notify_authorities() - It tests the notify_authorities() method of the SecuritySystem class. Set the armed attribute of the SecuritySystem object to True, call the notify_authorities() method, and verify that the returned value is 'Notifying authorities of a security breach...'. Then, set the armed attribute of the SecuritySystem object to False, call the notify_authorities() method again, and verify that the returned value is 'System is not armed.' - You should use two assertion methods.

# test_detect_breach() - It tests the detect_breach() method of the SecuritySystem class. Call the detect_breach() method of the SecuritySystem object and verify that the returned value is False. Then, set the armed attribute of the SecuritySystem object to True and set the breach_detected attribute of the first sensor object to True, call the detect_breach() method again, and verify that the returned value is True. - You should use two assertion methods.


# You should use a total of six assertion methods.

# Solution 22
# import unittest
# from security_system import SecuritySystem
# from camera import Camera
# from sensor import Sensor
# from alarm import Alarm


# class TestSecuritySystem(unittest.TestCase):
#     def setUp(self):
#         self.cameras = [
#             Camera('Front Door'),
#             Camera('Back Door'),
#             Camera('Garage'),
#         ]
#         self.sensors = [Sensor('Window Sensor'), Sensor('Motion Sensor')]
#         self.alarms = [Alarm('Main Alarm'), Alarm('Backup Alarm')]
#         self.system = SecuritySystem(
#             self.cameras, self.sensors, self.alarms
#         )

#     def test_arm(self):
#         self.system.arm()
#         self.assertTrue(self.system.armed)

#     def test_disarm(self):
#         self.system.armed = True
#         self.system.disarm()
#         self.assertFalse(self.system.armed)

#     def test_notify_authorities(self):
#         self.system.armed = True
#         self.assertEqual(
#             self.system.notify_authorities(),
#             'Notifying authorities of a security breach...',
#         )

#         self.system.armed = False
#         self.assertEqual(
#             self.system.notify_authorities(), 'System is not armed.'
#         )

#     def test_detect_breach(self):
#         self.assertFalse(self.system.detect_breach())

#         self.system.armed = True
#         self.system.sensors[0].breach_detected = True
#         self.assertTrue(self.system.detect_breach())
# ==================================================================================
if __name__ == '__main__':
    unittest.main(verbosity=2)
