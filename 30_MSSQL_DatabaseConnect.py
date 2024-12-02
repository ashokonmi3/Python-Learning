import pandas as pd
import pyodbc
# ================================
# DB creation
# Connection details
# server = 'localhost'  # Replace with your server name or IP
# username = 'root'       # Replace with your SQL Server username
# password = 'root123'  # Replace with your SQL Server password
# connection = None
# # Establish connection to the SQL Server (not to a specific database)
# try:
#     # Establish connection to the SQL Server with autocommit enabled
#     connection = pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};UID={username};PWD={password}",
#         autocommit=True
#     )
#     print("Connected to SQL Server!")

#     # Create a cursor
#     cursor = connection.cursor()

#     # Define the SQL query to create a database
#     db_name = 'MyNewDatabase'
#     create_db_query = f"CREATE DATABASE {db_name}"

#     # Execute the query
#     cursor.execute(create_db_query)
#     print(f"Database '{db_name}' created successfully!")

# except Exception as e:
#     print("Error:", e)

# finally:
#     # Close the connection
#     if connection:
#         connection.close()
#         print("Connection closed.")
# ===========================================
# Creating table
# import pyodbc

# # Connection details
# server = 'localhost'
# database = 'MyNewDatabase'  # The database you created earlier
# username = 'root'           # Your username
# password = 'root123'        # Your password

# try:
#     # Establish connection to the database with autocommit enabled
#     connection = pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}",
#         autocommit=True
#     )
#     print("Connected to the database!")

#     # Create a cursor
#     cursor = connection.cursor()

#     # Check if the table exists and drop it if it does
#     cursor.execute("IF OBJECT_ID('Users', 'U') IS NOT NULL DROP TABLE Users;")
#     print("Dropped existing 'Users' table (if it existed).")

#     # Define SQL query to create a table
#     create_table_query = """
#     CREATE TABLE Users (
#         ID INT PRIMARY KEY IDENTITY(1,1),
#         Name NVARCHAR(50),
#         Age INT,
#         Email NVARCHAR(50)
#     )
#     """
#     cursor.execute(create_table_query)
#     print("Table 'Users' created successfully!")

# except Exception as e:
#     print("Error while creating table:", e)

# finally:
#     # Close the connection
#     if connection:
#         connection.close()
#         print("Connection closed.")

# ===============================
# Reading tables in db
# import pyodbc

# # Connection details
# server = 'localhost'        # Replace with your server name
# database = 'MyNewDatabase'  # Replace with your database name
# username = 'root'           # Replace with your SQL Server username
# password = 'root123'        # Replace with your SQL Server password

# try:
#     # Establish connection to the database
#     connection = pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
#     )
#     print("Connected to the database!")

#     # Create a cursor
#     cursor = connection.cursor()

#     # Query to list all tables in the database
#     cursor.execute("""
#         SELECT TABLE_NAME
#         FROM INFORMATION_SCHEMA.TABLES
#         WHERE TABLE_TYPE = 'BASE TABLE';
#     """)

#     # Fetch and display the table names
#     tables = cursor.fetchall()
#     print("Tables in the database:")
#     for table in tables:
#         print(f"- {table.TABLE_NAME}")

# except Exception as e:
#     print("Error:", e)

# finally:
#     # Close the connection
#     if connection:
#         connection.close()
#         print("Connection closed.")


# ===============================
# insert data


# import pyodbc

# # Connection details
# server = 'localhost'
# database = 'MyNewDatabase'
# username = 'root'
# password = 'root123'

# try:
#     # Establish connection to the database
#     connection = pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
#     )
#     print("Connected to the database!")

#     # Create a cursor
#     cursor = connection.cursor()

#     # Insert data into the Users table
#     insert_query = """
#     INSERT INTO Users (Name, Age, Email)
#     VALUES (?, ?, ?)
#     """
#     data = [
#         ('Alice', 30, 'alice@example.com'),
#         ('Bob', 25, 'bob@example.com'),
#         ('Charlie', 35, 'charlie@example.com')
#     ]

#     for record in data:
#         cursor.execute(insert_query, record)

#     # Commit the transaction
#     connection.commit()
#     print("Data inserted successfully!")

# except Exception as e:
#     print("Error:", e)

# finally:
#     # Close the connection
#     if connection:
#         connection.close()
#         print("Connection closed.")
# =============================
# import pyodbc

# # Connection details
# server = 'localhost'        # Replace with your server name
# database = 'MyNewDatabase'  # Replace with your database name
# username = 'root'           # Replace with your SQL Server username
# password = 'root123'        # Replace with your password

# try:
#     # Establish connection to the database
#     connection = pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
#     )
#     print("Connected to the database!")

#     # Create a cursor
#     cursor = connection.cursor()

#     # Define the SQL query to read data
#     select_query = "SELECT * FROM Users"

#     # Execute the query
#     cursor.execute(select_query)

#     # Fetch all rows
#     rows = cursor.fetchall()

#     # Print the data
#     print("Data in 'Users' table:")
#     for row in rows:
#         print(
#             f"ID: {row.ID}, Name: {row.Name}, Age: {row.Age}, Email: {row.Email}")

# except Exception as e:
#     print("Error while reading data:", e)

# finally:
#     # Close the connection
#     if connection:
#         connection.close()
#         print("Connection closed.")
# ==============================

# Connection details
# server = 'localhost'        # Replace with your server name
# database = 'MyNewDatabase'  # Replace with your database name
# username = 'root'           # Replace with your SQL Server username
# password = 'root123'        # Replace with your password

# try:
#     # Establish connection to the database
#     connection = pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
#     )
#     print("Connected to the database!")

#     # Define the SQL query to fetch data
#     query = "SELECT * FROM Users"

#     # Load data into a Pandas DataFrame
#     df = pd.read_sql(query, connection)

#     # Display the DataFrame
#     print("Data in 'Users' table:")
#     print(df)

# except Exception as e:
#     print("Error while fetching data:", e)

# finally:
#     # Close the connection
#     if connection:
#         connection.close()
#         print("Connection closed.")
# ====================================
# Fetching all records
# import pyodbc

# # Connection details
# server = 'localhost'
# database = 'MyNewDatabase'
# username = 'root'
# password = 'root123'

# try:
#     connection = pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}")
#     print("Connected to the database!")

#     cursor = connection.cursor()

#     # SELECT query
#     query = "SELECT * FROM Users"
#     cursor.execute(query)

#     print("Data in 'Users' table:")
#     for row in cursor.fetchall():
#         print(
#             f"ID: {row.ID}, Name: {row.Name}, Age: {row.Age}, Email: {row.Email}")

# except Exception as e:
#     print("Error:", e)

# finally:
#     if connection:
#         connection.close()
#         print("Connection closed.")
# ===============================
# Fetching a specific column
# import pyodbc

# # Connection details
# server = 'localhost'
# database = 'MyNewDatabase'
# username = 'root'
# password = 'root123'

# try:
#     connection = pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}")
#     print("Connected to the database!")

#     cursor = connection.cursor()

#     # SELECT query for specific columns
#     query = "SELECT Name, Email FROM Users"
#     cursor.execute(query)

#     print("Data in 'Users' table:")
#     for row in cursor.fetchall():
#         print(f"Name: {row.Name}, Email: {row.Email}")

# except Exception as e:
#     print("Error:", e)

# finally:
#     if connection:
#         connection.close()
#         print("Connection closed.")
# =============================
# filter data
# import pyodbc

# # Connection details
# server = 'localhost'
# database = 'MyNewDatabase'
# username = 'root'
# password = 'root123'

# try:
#     connection = pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}")
#     print("Connected to the database!")

#     cursor = connection.cursor()

#     # SELECT query with a filter
#     query = "SELECT * FROM Users WHERE Age > 30"
#     cursor.execute(query)

#     print("Filtered Data in 'Users' table:")
#     for row in cursor.fetchall():
#         print(
#             f"ID: {row.ID}, Name: {row.Name}, Age: {row.Age}, Email: {row.Email}")

# except Exception as e:
#     print("Error:", e)

# finally:
#     if connection:
#         connection.close()
#         print("Connection closed.")
# ======================
# Add a new record


# # Connection details
# server = 'localhost'
# database = 'MyNewDatabase'
# username = 'root'
# password = 'root123'

# try:
#     connection = pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}")
#     print("Connected to the database!")

#     cursor = connection.cursor()

#     # INSERT query
#     query = "INSERT INTO Users (Name, Age, Email) VALUES ('David', 28, 'david@example.com')"
#     cursor.execute(query)
#     connection.commit()

#     print("Record inserted successfully!")

# except Exception as e:
#     print("Error:", e)

# finally:
#     if connection:
#         connection.close()
#         print("Connection closed.")

# =========================
# Modify the record

# # Connection details
# server = 'localhost'
# database = 'MyNewDatabase'
# username = 'root'
# password = 'root123'

# try:
#     connection = pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}")
#     print("Connected to the database!")

#     cursor = connection.cursor()

#     # UPDATE query
#     query = "UPDATE Users SET Age = 29 WHERE Name = 'David'"
#     cursor.execute(query)
#     connection.commit()

#     print("Record updated successfully!")

# except Exception as e:
#     print("Error:", e)

# finally:
#     if connection:
#         connection.close()
#         print("Connection closed.")
# =======================
# Remove a record
# import pyodbc

# # Connection details
# server = 'localhost'
# database = 'MyNewDatabase'
# username = 'root'
# password = 'root123'

# try:
#     connection = pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}")
#     print("Connected to the database!")

#     cursor = connection.cursor()

#     # DELETE query
#     query = "DELETE FROM Users WHERE Name = 'David'"
#     cursor.execute(query)
#     connection.commit()

#     print("Record deleted successfully!")

# except Exception as e:
#     print("Error:", e)

# finally:
#     if connection:
#         connection.close()
#         print("Connection closed.")
# ======================
# Count a record

# import pyodbc

# # Connection details
# server = 'localhost'
# database = 'MyNewDatabase'
# username = 'root'
# password = 'root123'

# try:
#     connection = pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}")
#     print("Connected to the database!")

#     cursor = connection.cursor()

#     # COUNT query
#     query = "SELECT COUNT(*) AS TotalUsers FROM Users"
#     cursor.execute(query)

#     total_users = cursor.fetchone()
#     print(f"Total users: {total_users.TotalUsers}")

# except Exception as e:
#     print("Error:", e)

# finally:
#     if connection:
#         connection.close()
#         print("Connection closed.")
# ======================
# Order by

# import pyodbc

# # Connection details
# server = 'localhost'
# database = 'MyNewDatabase'
# username = 'root'
# password = 'root123'

# try:
#     connection = pyodbc.connect(
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}")
#     print("Connected to the database!")

#     cursor = connection.cursor()

#     # ORDER BY query
#     query = "SELECT * FROM Users ORDER BY Age DESC"
#     cursor.execute(query)

#     print("Sorted Data in 'Users' table:")
#     for row in cursor.fetchall():
#         print(
#             f"ID: {row.ID}, Name: {row.Name}, Age: {row.Age}, Email: {row.Email}")

# except Exception as e:
#     print("Error:", e)

# finally:
#     if connection:
#         connection.close()
#         print("Connection closed.")
# ============================

# import pyodbc
# import logging

# # Configure logging
# logging.basicConfig(
#     filename='db_operations.log',
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# # Database connection details
# server = 'localhost'
# database = 'MyNewDatabase'
# username = 'root'
# password = 'root123'


# def connect_to_database():
#     """Establishes a connection to the database."""
#     try:
#         connection = pyodbc.connect(
#             f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
#         )
#         logging.info("Connected to the database.")
#         return connection
#     except pyodbc.Error as e:
#         logging.error("Error connecting to the database: %s", e)
#         return None


# def create_table(connection):
#     """Creates a Users table."""
#     try:
#         cursor = connection.cursor()
#         cursor.execute(
#             "IF OBJECT_ID('Users', 'U') IS NOT NULL DROP TABLE Users;")
#         cursor.execute("""
#             CREATE TABLE Users (
#                 ID INT PRIMARY KEY IDENTITY(1,1),
#                 Name NVARCHAR(50),
#                 Age INT,
#                 Email NVARCHAR(50)
#             );
#         """)
#         logging.info("Table 'Users' created successfully.")
#     except pyodbc.Error as e:
#         logging.error("Error creating table: %s", e)


# def insert_data(connection):
#     """Inserts sample data into the Users table."""
#     try:
#         cursor = connection.cursor()
#         data = [
#             ('Alice', 30, 'alice@example.com'),
#             ('Bob', 25, 'bob@example.com'),
#             ('Charlie', 35, 'charlie@example.com')
#         ]
#         cursor.executemany(
#             "INSERT INTO Users (Name, Age, Email) VALUES (?, ?, ?)", data)
#         connection.commit()
#         logging.info("Sample data inserted successfully.")
#     except pyodbc.Error as e:
#         logging.error("Error inserting data: %s", e)


# def read_data(connection):
#     """Fetches and prints all data from the Users table."""
#     try:
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM Users;")
#         rows = cursor.fetchall()
#         print("Users Data:")
#         for row in rows:
#             print(
#                 f"ID: {row.ID}, Name: {row.Name}, Age: {row.Age}, Email: {row.Email}")
#     except pyodbc.Error as e:
#         logging.error("Error reading data: %s", e)


# def update_data(connection):
#     """Updates the age of a specific user."""
#     try:
#         cursor = connection.cursor()
#         cursor.execute("UPDATE Users SET Age = 28 WHERE Name = 'Bob';")
#         connection.commit()
#         logging.info("Data updated successfully for user 'Bob'.")
#     except pyodbc.Error as e:
#         logging.error("Error updating data: %s", e)


# def delete_data(connection):
#     """Deletes a specific user."""
#     try:
#         cursor = connection.cursor()
#         cursor.execute("DELETE FROM Users WHERE Name = 'Charlie';")
#         connection.commit()
#         logging.info("Data deleted successfully for user 'Charlie'.")
#     except pyodbc.Error as e:
#         logging.error("Error deleting data: %s", e)


# def count_users(connection):
#     """Counts the total number of users."""
#     try:
#         cursor = connection.cursor()
#         cursor.execute("SELECT COUNT(*) AS TotalUsers FROM Users;")
#         count = cursor.fetchone().TotalUsers
#         print(f"Total Users: {count}")
#         logging.info("Counted total users: %d", count)
#     except pyodbc.Error as e:
#         logging.error("Error counting users: %s", e)


# def sort_users(connection):
#     """Fetches and prints users sorted by age."""
#     try:
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM Users ORDER BY Age DESC;")
#         rows = cursor.fetchall()
#         print("Users Sorted by Age:")
#         for row in rows:
#             print(
#                 f"ID: {row.ID}, Name: {row.Name}, Age: {row.Age}, Email: {row.Email}")
#     except pyodbc.Error as e:
#         logging.error("Error sorting users: %s", e)


# def main():
#     """Main function to execute all operations."""
#     connection = connect_to_database()
#     if connection:
#         try:
#             create_table(connection)
#             insert_data(connection)
#             print("\n--- Reading Data ---")
#             read_data(connection)
#             print("\n--- Updating Data ---")
#             update_data(connection)
#             print("\n--- Reading Data After Update ---")
#             read_data(connection)
#             print("\n--- Deleting Data ---")
#             delete_data(connection)
#             print("\n--- Reading Data After Deletion ---")
#             read_data(connection)
#             print("\n--- Counting Users ---")
#             count_users(connection)
#             print("\n--- Sorting Users by Age ---")
#             sort_users(connection)
#         finally:
#             connection.close()
#             logging.info("Connection closed.")
#             print("Connection closed.")


# if __name__ == "__main__":
#     main()
# ==============================

import pyodbc
import logging

# Configure logging
logging.basicConfig(
    filename='db_operations.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class DatabaseManager:
    """Class to manage database operations."""

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        """Establish a connection to the database."""
        try:
            self.connection = pyodbc.connect(
                f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
            )
            logging.info("Connected to the database.")
        except pyodbc.Error as e:
            logging.error("Error connecting to the database: %s", e)
            raise

    def disconnect(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            logging.info("Connection closed.")

    def create_table(self):
        """Create the Users table."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "IF OBJECT_ID('Users', 'U') IS NOT NULL DROP TABLE Users;")
            cursor.execute("""
                CREATE TABLE Users (
                    ID INT PRIMARY KEY IDENTITY(1,1),
                    Name NVARCHAR(50),
                    Age INT,
                    Email NVARCHAR(50)
                );
            """)
            logging.info("Table 'Users' created successfully.")
        except pyodbc.Error as e:
            logging.error("Error creating table: %s", e)

    def insert_data(self, data):
        """Insert data into the Users table."""
        try:
            cursor = self.connection.cursor()
            cursor.executemany(
                "INSERT INTO Users (Name, Age, Email) VALUES (?, ?, ?)", data)
            self.connection.commit()
            logging.info("Data inserted successfully.")
        except pyodbc.Error as e:
            logging.error("Error inserting data: %s", e)

    def read_data(self):
        """Fetch and print all data from the Users table."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Users;")
            rows = cursor.fetchall()
            print("Users Data:")
            for row in rows:
                print(
                    f"ID: {row.ID}, Name: {row.Name}, Age: {row.Age}, Email: {row.Email}")
        except pyodbc.Error as e:
            logging.error("Error reading data: %s", e)

    def update_data(self, name, new_age):
        """Update the age of a specific user."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "UPDATE Users SET Age = ? WHERE Name = ?", (new_age, name))
            self.connection.commit()
            logging.info(f"Data updated successfully for user '{name}'.")
        except pyodbc.Error as e:
            logging.error("Error updating data: %s", e)

    def delete_data(self, name):
        """Delete a specific user."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Users WHERE Name = ?", (name,))
            self.connection.commit()
            logging.info(f"Data deleted successfully for user '{name}'.")
        except pyodbc.Error as e:
            logging.error("Error deleting data: %s", e)

    def count_users(self):
        """Count the total number of users."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT COUNT(*) AS TotalUsers FROM Users;")
            count = cursor.fetchone().TotalUsers
            print(f"Total Users: {count}")
            logging.info("Counted total users: %d", count)
        except pyodbc.Error as e:
            logging.error("Error counting users: %s", e)

    def sort_users(self):
        """Fetch and print users sorted by age."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Users ORDER BY Age DESC;")
            rows = cursor.fetchall()
            print("Users Sorted by Age:")
            for row in rows:
                print(
                    f"ID: {row.ID}, Name: {row.Name}, Age: {row.Age}, Email: {row.Email}")
        except pyodbc.Error as e:
            logging.error("Error sorting users: %s", e)


def main():
    """Main function to execute database operations."""
    # Database connection details
    db_manager = DatabaseManager(
        server='localhost',
        database='MyNewDatabase',
        username='root',
        password='root123'
    )

    try:
        db_manager.connect()
        db_manager.create_table()

        # Insert sample data
        sample_data = [
            ('Alice', 30, 'alice@example.com'),
            ('Bob', 25, 'bob@example.com'),
            ('Charlie', 35, 'charlie@example.com')
        ]
        db_manager.insert_data(sample_data)

        # Perform operations
        print("\n--- Reading Data ---")
        db_manager.read_data()

        print("\n--- Updating Data ---")
        db_manager.update_data('Bob', 28)
        db_manager.read_data()

        print("\n--- Deleting Data ---")
        db_manager.delete_data('Charlie')
        db_manager.read_data()

        print("\n--- Counting Users ---")
        db_manager.count_users()

        print("\n--- Sorting Users by Age ---")
        db_manager.sort_users()

    except Exception as e:
        print("An error occurred:", e)
    finally:
        db_manager.disconnect()


if __name__ == "__main__":
    main()
