# pip install sqlite3
# My sql password root123
# print SELECT SQLITE_VERSION();

# .exit

# ls -la the database will be created
#
# from sqlite3 import *
# import mysql.connector
# import sqlite3
# import sys

# conn = sqlite3.connect('test.db')
# print("Opened database successfully")
# print(type(conn))
# # conn = sqlite3.connect('my_database233231.db')

# # # print dir(conn)
# conn.execute('''CREATE TABLE COMPANY0022111
#             (ID INT PRIMARY KEY     NOT NULL,
#             NAME           TEXT    NOT NULL,
#             AGE            INT     NOT NULL,
#             ADDRESS        CHAR(50),
#             SALARY         REAL);''')


# print("Table created successfully")
# conn.execute("INSERT INTO COMPANY0022 (ID,NAME,AGE,ADDRESS,SALARY) \
#         VALUES (1, 'Paul', 32, 'California', 20000.00 )")
# conn.close()
# ==========================
# The DB-API spec requires that connecting to the database begins a new transaction, by default. You must commit to confirm any changes you make, or rollback to discard them.
#

# import sqlite3

# conn = sqlite3.connect('test.db',)
# print("Opened database successfully")
# conn.execute("INSERT INTO COMPANY0022111 (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (14, 'Paul', 32, 'California', 20000.00 )")

# conn.execute("INSERT INTO COMPANY0022111 (ID,NAME,AGE,ADDRESS,SALARY) \
#      VALUES (5, 'Allen', 25, 'Texas', 15000.00 )")

# conn.execute("INSERT INTO COMPANY0022111 (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (6, 'Teddy', 23, 'Norway', 20000.00 )")

# conn.execute("INSERT INTO COMPANY0022111 (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (7, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

# conn.commit()
# # print "Records created successfully";
# conn.close()

# ========================
# import sqlite3

# conn = sqlite3.connect('test.db')
# print("Opened database successfully")

# cursor = conn.execute("SELECT id, name, address, salary from COMPANY0022111")
# # # print type(cursor)
# for a in cursor:
#     print(a)
#     print("ID = ", a[0])
#     print("NAME = ", a[1])
#     print("ADDRESS = ", a[2])
#     print("SALARY = ", a[3], "\n")

# print("Operation done successfully")
# conn.close()

# =============================
# for oracle
# pip install cx_Oracle
# import cx_Oracle
# print (dir(cx_Oracle))
# ip = '192.168.0.1'
# port = 1521
# SID = 'YOURSIDHERE'
# dsn_tns = cx_Oracle.makedsn(ip, port, SID)
# db = cx_Oracle.connect('username', 'password', dsn_tns)
# connstr = 'usrname/password@server_IP:1521/orcl'

# con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')
# print con.version
# con.close()
#
# cnx = mysql.connector.connect(user='joe', database='test')
# cnx = MySQLConnection(user='joe', database='test')
# #
#
# ===============================
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="root123"
# )

# print(mydb)

# ========================================
# create a database named "mydatabase":
# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="root123"
# )

# # print(mydb)#
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")

# ====================
# You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement:

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="root123"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)

# ======================

# you can try to access the database when making the connection:

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="root123",
#   database="mydatabase"
# )

# =========================
# Create a table named "customers":

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="root123",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# =======================================
# You can check if a table exist by listing all tables in your database with the "SHOW TABLES" statement:


# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="root123",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)

# ============================
# create table with primary key

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="root123",
#     database="mydatabase5"
# )

# mycursor = mydb.cursor()

# mycursor.execute(
#     "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# ==========================
# If the table already exists, use the ALTER TABLE keyword:

# Example
# Create primary key on an existing table:


# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   passwd="yourpassword",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# ===============================
# Insert Into Table
# To fill a table in MySQL, use the "INSERT INTO" statement.

# Example
# Insert a record in the "customers" table:

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="root123",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()
# # Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

# print(mycursor.rowcount, "record inserted.")

# ===========================

# Insert Multiple Rows
# To insert multiple rows into a table, use the executemany() method.

# The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:

# Example
# Fill the "customers" table with data:

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="root123",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")


# =============================


# Select From a Table
# To select from a table in MySQL, use the "SELECT" statement:

# Example
# Select all records from the "customers" table, and display the result:

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="root123",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
# ============================
# Selecting Columns
# To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):

# Example
# Select only the name and address columns:

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   passwd="yourpassword",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SELECT name, address FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
# ==============================
# Using the fetchone() Method
# If you are only interested in one row, you can use the fetchone() method.

# The fetchone() method will return the first row of the result:

# Example
# Fetch only one row:

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="root123",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchone()

# print(myresult)
# =================================

# Delete Record
# You can delete records from an existing table by using the "DELETE FROM" statement:

# Example
# Delete any record where the address is "Mountain 21":

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   passwd="yourpassword",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")
# ==========================

# Delete a Table
# You can delete an existing table by using the "DROP TABLE" statement:

# Example
# Delete the table "customers":

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   passwd="yourpassword",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# sql = "DROP TABLE customers"

# mycursor.execute(sql)

# ===================

# Update Table
# You can update existing records in a table by using the "UPDATE" statement:

# Example
# Overwrite the address column from "Valley 345" to "Canyoun 123":

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   passwd="yourpassword",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")
# ======================
# Passing parameter in query
# Connect to the database
connection = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_database"
)

# Create a cursor object
cursor = connection.cursor()

# Example data
user_id = 1
user_name = "John Doe"

# SQL query with placeholders
sql_query = "INSERT INTO users (id, name) VALUES (%s, %s)"

# Execute the query with parameters
cursor.execute(sql_query, (user_id, user_name))

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
