Exercise 1
The implementation of the Product class is given in the product.py file. In the solution file (exercise.py) to the TestProduct class add a setUp() method that creates the following instance of the Product class: Product('milk', 3.0) and assigns it to an attribute named product of the TestProduct class.

Then implement the following test methods in the TestProduct class:

test_get_product_name() checks if the value of the name attribute is equal to 'milk'

test_get_product_price() checks if the value of the price attribute is equal to 3.0

test_get_quantity() checks if the value of the quantity attribute is equal to 1



You only need to define the class and the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.



Solution 1
import unittest
from product import Product
 
 
class TestProduct(unittest.TestCase):
    def setUp(self) -> None:
        self.product = Product(name="milk", price=3.0)
 
    def test_get_product_name(self) -> None:
        self.assertEqual(self.product.name, "milk")
 
    def test_get_product_price(self) -> None:
        self.assertEqual(self.product.price, 3.0)
 
    def test_get_quantity(self) -> None:
        self.assertEqual(self.product.quantity, 1)

==================================================================================
Exercise 2
The implementation of the Product class is given in the product.py file. In the solution file (exercise.py) add a test method to the TestProduct class that validates the __repr__() method named test_repr_method().



You only need to define the appropriate test. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.



Solution 2
import unittest
from product import Product
 
 
class TestProduct(unittest.TestCase):
    def setUp(self) -> None:
        self.product = Product(name="milk", price=3.0)
 
    def test_get_product_name(self) -> None:
        self.assertEqual(self.product.name, "milk")
 
    def test_get_product_price(self) -> None:
        self.assertEqual(self.product.price, 3.0)
 
    def test_get_quantity(self) -> None:
        self.assertEqual(self.product.quantity, 1)
 
    def test_repr_method(self) -> None:
        self.assertEqual(
            repr(self.product),
            "Product(name='milk', price=3.0, quantity=1)",
            "Product's __repr__ method did not return expected result"
        )


==================================================================================

Exercise 3
The implementation of the Product class is given in the product.py file and the implementation of the ShoppingBasket class is given in the basket.py file.

In the solution file (exercise.py) create a TestBasketWithNoProducts class that inherits from unittest.TestCase and implements the following test methods for a shopping basket without products:

test_size_of_basket_should_be_empty() - checks if the basket size is 0


test_getting_product_out_of_range_should_raise_error() - checks if IndexError is raised when trying to get the product with index 0


test_total_amount_should_be_zero() - checks if the total value of the basket is equal to 0



Also add the setUpClass() method of the TestBasketWithNoProducts class that creates an instance of the ShoppingBasket class and assigns it as an attribute of the TestBasketWithNoProducts class named basket.



You only need to define the class and the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.



Solution 3
import unittest
from basket import ShoppingBasket
 
 
class TestBasketWithNoProducts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket()
 
    def test_size_of_basket_should_be_empty(self):
        self.assertEqual(len(self.basket), 0)
 
    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(0)
 
    def test_total_amount_should_be_zero(self):
        self.assertEqual(self.basket.total(), 0.0)


==================================================================================
Exercise 4
The implementation of the Product class is given in the product.py file and the implementation of the ShoppingBasket class is given in the basket.py file.



In the solution file (exercise.py) create a TestBasketWithOneProduct class that inherits from unittest.TestCase. To this class add a setUpClass() method that creates an instance of the ShoppingBasket class and assigns it as an attribute of the TestBasketWithOneProduct named basket. Add one product with the following arguments to this instance:

name='milk', price=3.0

Implement the following test methods in the TestBasketWithOneProduct class:

test_size_of_basket_should_be_one() - checks if the basket size is equal to 1


test_total_amount_should_have_tax() - checks if the total basket value is equal to 3.63


test_getting_product() - checks if the product name with index 0 is 'milk' -> use get_product() method for this


test_getting_product_out_of_range_should_raise_error() - checks if we get IndexError when we try to read the product with index 1



You only need to define the class and the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.



Solution 4
import unittest
from basket import ShoppingBasket
 
 
class TestBasketWithNoProducts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket()
 
    def test_size_of_basket_should_be_empty(self):
        self.assertEqual(len(self.basket), 0)
 
    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(0)
 
    def test_total_amount_should_be_zero(self):
        self.assertEqual(self.basket.total(), 0.0)
 
 
class TestBasketWithOneProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket().add_product(name="milk", price=3.0)
 
    def test_size_of_basket_should_be_one(self):
        self.assertEqual(len(self.basket), 1)
 
    def test_total_amount_should_have_tax(self):
        self.assertEqual(self.basket.total(), 3.63)
 
    def test_getting_product(self):
        self.assertEqual(self.basket.get_product(0).name, "milk")
 
    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(1)


==================================================================================
Exercise 5
The implementation of the Product class is given in the product.py file and the implementation of the ShoppingBasket class is given in the basket.py file.



In the solution file (exercise.py) create a TestBasketWithTwoProducts class that inherits from unittest.TestCase. To this class add a setUpClass() method that creates an instance of the ShoppingBasket class and assigns it as an attribute of the TestBasketWithTwoProducts class named basket. Add two products with the following arguments to this instance:

name='milk', price=3.0

name='water', price=2.0



Implement the following test methods for the TestBasketWithTwoProducts class:

test_size_of_basket_should_be_two() - checks if the basket size is equal to 2


test_order_of_products() - checks if the order of products is consistent -> use get_product() method for this


test_total_amount_should_have_tax() - checks if the total basket value is equal to 6.05


test_getting_product_out_of_range_should_raise_error() - checks if we get IndexError when trying to get the product with index 2



You only need to define the class and the appropriate tests. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.



Solution 5
import unittest
from basket import ShoppingBasket
 
 
class TestBasketWithNoProducts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket()
 
    def test_size_of_basket_should_be_empty(self):
        self.assertEqual(len(self.basket), 0)
 
    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(0)
 
    def test_total_amount_should_be_zero(self):
        self.assertEqual(self.basket.total(), 0.0)
 
 
class TestBasketWithOneProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket().add_product(name="milk", price=3.0)
 
    def test_size_of_basket_should_be_one(self):
        self.assertEqual(len(self.basket), 1)
 
    def test_total_amount_should_have_tax(self):
        self.assertEqual(self.basket.total(), 3.63)
 
    def test_getting_product(self):
        self.assertEqual(self.basket.get_product(0).name, "milk")
 
    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(1)
 
 
class TestBasketWithTwoProducts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket() \
            .add_product(name="milk", price=3.0) \
            .add_product(name="water", price=2.0)
 
    def test_size_of_basket_should_be_two(self) -> None:
        self.assertEqual(len(self.basket), 2)
 
    def test_order_of_products(self):
        self.assertEqual(self.basket.get_product(0).name, "milk")
        self.assertEqual(self.basket.get_product(0).price, 3.0)
        self.assertEqual(self.basket.get_product(1).name, "water")
        self.assertEqual(self.basket.get_product(1).price, 2.0)
 
    def test_total_amount_should_have_tax(self):
        self.assertEqual(self.basket.total(), 6.05)
 
    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(2)

==================================================================================

