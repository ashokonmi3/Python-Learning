import os
import sys
from datetime import date
import unittest

# Exercise 1
# The following code is given:


# import unittest


# class Container:
#     code = 'ABCD1234'


# class TestContainer(unittest.TestCase):
#     def test_container_is_instance_of_type(self) -> None:
#         self.assertIsInstance(Container, type)

#     def test_container_has_code_attribute(self) -> None:
#         msg = 'The Container class does not have a code attribute.'
#         self.assertTrue(hasattr(Container, 'code'), msg)


# Modify the implementation of the TestContainer class so that the test_container_has_code_attribute()
# test is skipped, passing the reason for the skipping:
# 'The Container class requires implementation.'
# Tip: Use the unittest.skip() decorator.

# You only need to modify the implementation of the TestContainer class.
# During the solution verification, the tests are run and in case of any errors,
# the test report will be printed to the console.


# Solution 1
import unittest


# class Container:
#     code = 'ABCD1234'


# class TestContainer(unittest.TestCase):
#     def test_container_is_instance_of_type(self) -> None:
#         self.assertIsInstance(Container, type)

#     @unittest.skip('The Container class requires implementation.')
#     def test_container_has_code_attribute(self) -> None:
#         msg = 'The Container class does not have a code attribute.'
#         self.assertTrue(hasattr(Container, 'code'), msg)

# ==================================================================================
# Exercise 2
# The following code is given:


# from datetime import date
# import unittest


# class Container:
#     def __init__(self):
#         if date.today().day % 2 == 0:
#             self.code = 'XC-0'
#         else:
#             self.code = 'XC-1'


# class TestContainer(unittest.TestCase):
#     def test_code_ends_with_0_on_even_days(self):
#         c = Container()
#         self.assertTrue(
#             c.code.endswith('0'), 'Expected code to end with 0.'
#         )

#     def test_code_ends_with_1_on_odd_days(self):
#         c = Container()
#         self.assertTrue(
#             c.code.endswith('1'), 'Expected code to end with 1.'
#         )


# Modify the implementation of the TestContainer class so that:

# test_code_ends_with_0_on_even_days() method execution is skipped on even days. Provide reason for skipping test: 'Skipping even days.'


# test_code_ends_with_1_on_odd_days() method execution is skipped on odd days. Provide reason for skipping test: 'Skipping odd days.'


# You only need to modify the implementation of the TestContainer class. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

# Solution 2


# class Container:
#     def __init__(self):
#         print(f"Todays day is {date.today().day}")
#         if date.today().day % 2 == 0:
#             self.code = 'XC-0'
#         else:
#             self.code = 'XC-1'


# class TestContainer(unittest.TestCase):
#     @unittest.skipIf(date.today().day % 2 != 0, 'Skipping odd days.')
#     def test_code_ends_with_0_on_even_days(self):
#         c = Container()
#         self.assertTrue(
#             c.code.endswith('0'), 'Expected code to end with 0.'
#         )

#     @unittest.skipIf(date.today().day % 2 == 0, 'Skipping even days.')
#     def test_code_ends_with_1_on_odd_days(self):
#         c = Container()
#         self.assertTrue(
#             c.code.endswith('1'), 'Expected code to end with 1.'
#         )

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
#     def test_code_is_XC_win_on_Windows(self):
#         c = Container()
#         self.assertEqual(c.code, 'XC-win', 'Expected code to be XC-win.')

#     def test_code_starts_with_XC_on_Linux(self):
#         c = Container()
#         self.assertEqual(
#             c.code, 'XC-linux', 'Expected code to be XC-linux.'
#         )


# Modify the implementation of the TestContainer class so that:

# test_code_is_XC_win_on_Windows() method only runs on Windows. Provide reason for skipping test: 'Requires Windows.'


# test_code_starts_with_XC_on_Linux() method only runs on Linux. Provide reason for skipping test: 'Requires Linux.'


# You only need to modify the implementation of the TestContainer class. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.


# Solution 3


class Container:
    def __init__(self):
        if sys.platform.startswith('win'):
            self.code = 'XC-win'
        else:
            self.code = f'XC-{sys.platform}'


class TestContainer(unittest.TestCase):
    @unittest.skipUnless(
        sys.platform.startswith('win'), 'Requires Windows.'
    )
    def test_code_is_XC_win_on_Windows(self):
        c = Container()
        self.assertEqual(c.code, 'XC-win', 'Expected code to be XC-win.')

    @unittest.skipUnless(
        sys.platform.startswith('linux'), 'Requires Linux.'
    )
    def test_code_starts_with_XC_on_Linux(self):
        c = Container()
        self.assertEqual(
            c.code, 'XC-linux', 'Expected code to be XC-linux.'
        )

# ==================================================================================

# Exercise 4
# Suppose you have a class called EmailSender that sends emails:


# class EmailSender:
#     def send_email(self, to, subject, body):
#         # Code to send email
#         return True


# Define a class called TestEmailSender that inherits from unittest.TestCase. Then define a test method called test_send_email(), which tests whether the send_email() method of the EmailSender class correctly sends an email.


# However, you should add a @unittest.skipIf decorator that checks whether the network is available before running the test - use is_network_available() function. If the network is not available, the test should be skipped with the message "Network unavailable".

# Solution 4
# Sample solution:

# import unittest


# class EmailSender:
#     def send_email(self, to, subject, body):
#         # Code to send email
#         return True


# def is_network_available():
#     # Code to check if network is available
#     return True


# class TestEmailSender(unittest.TestCase):
#     @unittest.skipIf(not is_network_available(), "Network unavailable")
#     def test_send_email(self):
#         sender = EmailSender()
#         result = sender.send_email(
#             "test@example.com", "My Subject", "My Body"
#         )
#         self.assertTrue(result)
# ==================================================================================

# Exercise 5
# Suppose you have a class called FileReader that reads data from a file:


# class FileReader:
#     def __init__(self, filename):
#         self.filename = filename

#     def read_data(self):
#         with open(self.filename, 'r') as f:
#             return f.read()


# Define a class called TestFileReader that inherits from unittest.TestCase. Then define a test method called test_read_data(), which tests whether the read_data() method of the FileReader class correctly reads data from a file.


# However, you should add a @unittest.skipUnless decorator that checks whether the file test.txt exists before running the test. If the file does not exist, the test should be skipped with the message "File not found".

# Solution 5


# class FileReader:
#     def __init__(self, filename):
#         self.filename = filename

#     def read_data(self):
#         with open(self.filename, 'r') as f:
#             return f.read()


# class TestFileReader(unittest.TestCase):
#     def setUp(self):
#         self.filename = 'test.txt'
#         with open(self.filename, 'w') as f:
#             f.write('Hello, world!')

#     def tearDown(self):
#         os.remove(self.filename)

#     @unittest.skipUnless(os.path.isfile('test.txt'), "File not found")
#     def test_read_data(self):
#         reader = FileReader(self.filename)
#         data = reader.read_data()
#         self.assertEqual(data, 'Hello, world!')
# ==================================================================================
# Exercise 6
# Suppose you have a class called DataTransformer that transforms data:


# class DataTransformer:
#     def transform(self, data):
#         # code to transform data
#         return transformed_data


# Define a class called TestDataTransformer that inherits from unittest.TestCase. Then define a test method called test_transform(), which tests whether the transform() method of the DataTransformer class correctly transforms data.


# However, you should add a @unittest.skip decorator to skip this test, with the message "Test skipped as not implemented yet".

# Solution 6
# import unittest


# class DataTransformer:
#     def transform(self, data):
#         # Code to transform data
#         transformed_data = "**********************"+data+"**********************"
#         return transformed_data


# class TestDataTransformer(unittest.TestCase):
#     @unittest.skip("Test skipped as not implemented yet")
#     def test_transform(self):
#         self.fail("Test not implemented yet")

# ==================================================================================

# Exercise 7
# Suppose you have a class called PaymentGateway that processes payments:


# class PaymentGateway:
#     def process_payment(self, amount):
#         # code to process payment
#         return True


# Define a class called TestPaymentGateway that inherits from unittest.TestCase. Then define a test method called test_process_payment(), which tests whether the process_payment() method of the PaymentGateway class correctly processes a payment.


# However, you should add a @unittest.skipIf decorator that checks whether the code is running in a production environment before running the test - use is_production_environment() function. If the code is not running in a production environment, the test is skipped with the message "Not in production environment".


# Solution 7


class PaymentGateway:
    def process_payment(self, amount):
        # Code to process payment
        return True


def is_production_environment():
    # Code to check if it is a production environment
    return True


class TestPaymentGateway(unittest.TestCase):
    @unittest.skipIf(
        not is_production_environment(),
        "Not in production environment",
    )
    def test_process_payment(self):
        gateway = PaymentGateway()
        result = gateway.process_payment(100.0)
        self.assertTrue(result)


# ==================================================================================
if __name__ == '__main__':
    unittest.main()
