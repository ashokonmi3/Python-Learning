
Exercise 1
The CustomersDB class is implemented in the customers.py file. The TestCustomersDB class is in the exercise.py file. Study carefully the implementation of both of these classes. Then add a test method to the TestCustomersDB class named:

test_add_customer(), which checks the add_customer() method of the CustomersDB class.

Steps:

In the test method create instance of the CustomersDB class:


db = CustomersDB(self.connection)


Call the add_customer() method on the db instance adding the following client:


'Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA'


Create an instance of the Cursor class named cursor.

Execute the following SQL code by calling the appropriate method of the Cursor class on the cursor instance:


SELECT *
FROM customers
ORDER BY first_name, last_name;


Assert the obtained result with the expected one.

Expected result:


expected = (
    ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
    ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
    ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
)


You only need to define the appropriate test. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

Solution 1
import unittest
import sqlite3
from customers import CustomersDB
 
 
class TestCustomersDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.cursor = cls.connection.cursor()
 
        create_table_sql = """
            CREATE TABLE customers 
            ( 
                first_name TEXT, 
                last_name  TEXT, 
                email      TEXT, 
                phone      TEXT, 
                country    TEXT 
            );"""
        cls.cursor.execute(create_table_sql)
 
        customers_data = [
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA')
        ]
 
        insert_sql = """
            INSERT INTO customers
            VALUES (?, ?, ?, ?, ?);"""
        cls.cursor.executemany(insert_sql, customers_data)
 
    @classmethod
    def tearDownClass(cls):
        cls.connection.close()
 
    def test_add_customer(self):
        db = CustomersDB(self.connection)
        db.add_customer('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM customers
            ORDER BY first_name, last_name;
        """)
 
        actual = cursor.fetchall()
        expected = [
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        ]
        self.assertEqual(actual, expected)

==================================================================================

Exercise 2
The CustomersDB class is implemented in the customers.py file. The TestCustomersDB class is in the exercise.py file. Study carefully the implementation of both of these classes. Then add a test method to the TestCustomersDB class named:

test_find_customers_by_first_name() which checks the find_customers_by_first_name() method of the CustomersDB class.

Steps:

In the test method create instance of the CustomersDB class:


db = CustomersDB(self.connection)


Call find_customers_by_first_name() on the db instance.

Assert the obtained result with the expected one.

Expected result:


expected = (
    ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
    ('John', 'Smith', 'john.smith@mail.com', '111', 'USA')
)


You only need to define the appropriate test. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.

Solution 2
import unittest
import sqlite3
from customers import CustomersDB
 
 
class TestCustomersDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.cursor = cls.connection.cursor()
 
        create_table_sql = """
            CREATE TABLE customers 
            ( 
                first_name TEXT, 
                last_name  TEXT, 
                email      TEXT, 
                phone      TEXT, 
                country    TEXT 
            );"""
        cls.cursor.execute(create_table_sql)
 
        customers_data = [
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        ]
 
        insert_sql = """
            INSERT INTO customers
            VALUES (?, ?, ?, ?, ?);"""
        cls.cursor.executemany(insert_sql, customers_data)
 
    @classmethod
    def tearDownClass(cls):
        cls.connection.close()
 
    def test_find_customers_by_first_name(self):
        db = CustomersDB(self.connection)
        actual = db.find_customers_by_first_name('John')
        expected = [
            ('John', 'Doe', 'john.doe@mail.com', '333', 'USA'),
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA')
        ]
        self.assertEqual(actual, expected)

==================================================================================

Exercise 3
The CustomersDB class is implemented in the customers.py file. The TestCustomersDB class is in the exercise.py file. Study carefully the implementation of both of these classes. Then add a test method to the TestCustomersDB class named:

test_find_customers_by_country() which checks the find_customers_by_country() method of the CustomersDB class.

Steps:

In the test method create instance of the CustomersDB class:


db = CustomersDB(self.connection)


Call the find_customers_by_country() method on the db instance.

Assert the obtained result with the expected one.

Expected result:


expected = (
    ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
    ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
)


You only need to define the appropriate test. During the solution verification, the tests are run and in case of any errors, the test report will be printed to the console.




Solution 3
import unittest
import sqlite3
from customers import CustomersDB
 
 
class TestCustomersDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.cursor = cls.connection.cursor()
 
        create_table_sql = """
            CREATE TABLE customers 
            ( 
                first_name TEXT, 
                last_name  TEXT, 
                email      TEXT, 
                phone      TEXT, 
                country    TEXT 
            );"""
        cls.cursor.execute(create_table_sql)
 
        customers_data = [
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'Canada'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        ]
 
        insert_sql = """
            INSERT INTO customers
            VALUES (?, ?, ?, ?, ?);"""
        cls.cursor.executemany(insert_sql, customers_data)
 
    @classmethod
    def tearDownClass(cls):
        cls.connection.close()
 
    def test_find_customers_by_country(self):
        db = CustomersDB(self.connection)
 
        actual = db.find_customers_by_country('USA')
        expected = [
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        ]
        self.assertEqual(actual, expected)

==================================================================================

