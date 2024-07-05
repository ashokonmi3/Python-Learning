
Exercise 1
Suppose you have a class called BankAccount that represents a bank account. The class has the following attributes: account_number (a string), balance (a float), and account_type (a string). The class has the following methods: deposit (which adds a given amount to the balance), withdraw (which subtracts a given amount from the balance), and transfer (which transfers a given amount from the account to another account). Your task is to write test cases for this class using unittest.



Here's an example implementation of the BankAccount class:



class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
 
    def deposit(self, amount):
        self.balance += amount
 
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
 
    def transfer(self, amount, account):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        account.deposit(amount)


Using the unittest framework create the unit test class named TestBankAccount and implement the following test methods:

test_deposit() - one assertion

test_withdraw() - one assertion

test_transfer() - two assertions



Choose the input data for the tests according to the description of the test methods. You should use a total of 4 assertion methods.



Solution 1
import unittest
from bank_account import BankAccount
 
 
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("111", 1000, "checking")
        self.account2 = BankAccount("222", 500, "savings")
 
    def test_deposit(self):
        self.account1.deposit(500)
        self.assertEqual(self.account1.balance, 1500)
 
    def test_withdraw(self):
        self.account1.withdraw(500)
        self.assertEqual(self.account1.balance, 500)
 
    def test_transfer(self):
        self.account1.transfer(500, self.account2)
        self.assertEqual(self.account1.balance, 500)
        self.assertEqual(self.account2.balance, 1000)

==================================================================================

Exercise 2
Suppose you have a class called BankAccount that represents a bank account. The class has the following attributes: account_number (a string), balance (a float), and account_type (a string). The class has the following methods: deposit (which adds a given amount to the balance), withdraw (which subtracts a given amount from the balance), and transfer (which transfers a given amount from the account to another account). Your task is to write test cases for this class using unittest.



Here's an example implementation of the BankAccount class:



class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
 
    def deposit(self, amount):
        self.balance += amount
 
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
 
    def transfer(self, amount, account):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        account.deposit(amount)


Using the unittest framework create the unit test class named TestBankAccount and implement the following test methods:

test_withdraw_insufficient_balance() - one assertion

test_transfer_insufficient_balance() - one assertion



Choose the input data for the tests according to the description of the test methods. You should use a total of 2 assertion methods.



Solution 2
import unittest
from bank_account import BankAccount
 
 
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("111", 1000, "checking")
        self.account2 = BankAccount("222", 500, "savings")
 
    def test_withdraw_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(1500)
 
    def test_transfer_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account1.transfer(1500, self.account2)

==================================================================================
Exercise 3
Suppose you have a class called BankAccount that represents a bank account. The class has the following attributes: account_number (a string), balance (a float), and account_type (a string). The class has the following methods: deposit (which adds a given amount to the balance), withdraw (which subtracts a given amount from the balance), and transfer (which transfers a given amount from the account to another account). You have added a new method to the BankAccount class called calculate_interest() that takes no input and returns the amount of interest earned on the account balance. The interest rate is 1.5% per year, compounded annually. Your task is to write test cases for this new method using unittest.



Here's an example implementation of the BankAccount class:



class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
 
    def deposit(self, amount):
        self.balance += amount
 
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
 
    def transfer(self, amount, account):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        account.deposit(amount)
 
    def calculate_interest(self):
        return round(self.balance * 0.015, 2)


Using the unittest framework create the unit test class named TestBankAccount and implement the following test method:

test_calculate_interest() - it should check if the calculate_interest() method returns the correct amount of interest earned on the account balance. You should test this method on two accounts with different initial balances and also test updating the balance and recalculating the interest.



Choose the input data for the tests according to the description of the test methods. You should use a total of 3 assertion methods.

Solution 3
import unittest
from bank_account import BankAccount
 
 
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("111", 1000, "checking")
        self.account2 = BankAccount("222", 500, "savings")
 
    def test_calculate_interest(self):
        self.assertEqual(self.account1.calculate_interest(), 15.0)
        self.assertEqual(self.account2.calculate_interest(), 7.5)
        self.account1.balance = 1500
        self.assertEqual(self.account1.calculate_interest(), 22.5)


==================================================================================
Exercise 4
Suppose you have a class called BankAccount that represents a bank account. The class has the following attributes: account_number (a string), balance (a float),account_type (a string), and overdraft_limit (a float). The overdraft_limit specifies the maximum amount that the account can go into overdraft. The class has the following methods: deposit (which adds a given amount to the balance), withdraw (which subtracts a given amount from the balance), and transfer (which transfers a given amount from the account to another account). Your task is to write test cases for this class using unittest.



Here's an example implementation of the BankAccount class:



class BankAccount:
    def __init__(self, account_number, balance, account_type, overdraft_limit=0):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.overdraft_limit = overdraft_limit
 
    def deposit(self, amount):
        self.balance += amount
 
    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Insufficient balance")
        self.balance -= amount
 
    def transfer(self, amount, account):
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        account.deposit(amount)


Using the unittest framework create the unit test class named TestBankAccount and implement the following test methods:

test_deposit() - it should tests the deposit() method by depositing some amount into two different accounts and checking if the balance has increased accordingly.

test_withdraw() - it should tests the withdraw() method by withdrawing some amount from two different accounts, checking if the balance has decreased accordingly, and verifying that a ValueError is raised if the requested amount exceeds the balance plus the overdraft limit.

test_transfer() - it should tests the transfer() method by transferring some amount from one account to the other, checking if the balances have been updated accordingly, and verifying that a ValueError is raised if the requested amount exceeds the balance plus the overdraft limit.



Choose the input data for the tests according to the description of the test methods.

Solution 4
import unittest
from bank_account import BankAccount
 
 
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("123456", 1000, "checking", 500)
        self.account2 = BankAccount("654321", 500, "savings", 1000)
 
    def test_deposit(self):
        self.account1.deposit(500)
        self.assertEqual(self.account1.balance, 1500)
        self.account2.deposit(1000)
        self.assertEqual(self.account2.balance, 1500)
 
    def test_withdraw(self):
        self.account1.withdraw(500)
        self.assertEqual(self.account1.balance, 500)
        self.assertRaises(ValueError, self.account1.withdraw, 1500)
        self.account2.withdraw(1000)
        self.assertEqual(self.account2.balance, -500)
 
    def test_transfer(self):
        self.account1.transfer(500, self.account2)
        self.assertEqual(self.account1.balance, 500)
        self.assertEqual(self.account2.balance, 1000)
        self.assertRaises(
            ValueError, self.account1.transfer, 1500, self.account2
        )
        self.account2.transfer(1500, self.account1)
        self.assertEqual(self.account1.balance, 2000)
        self.assertEqual(self.account2.balance, -500)


==================================================================================
