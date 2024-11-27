# Level	    Numeric Value	Description
# DEBUG	    10	            Detailed information, typically useful only for diagnosing problems.
# INFO	    20	            General information about the application's operation.
# WARNING	30	            Indication of potential problems or an abnormal situation.
# ERROR	    40	            Errors that occur during the application's execution.
# CRITICAL	50          	A very serious error that may prevent the program from continuing.


# import logging

# # Set up logging configuration
# logging.basicConfig(
#     format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# # Logging different levels
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")
# # ====================================
# import logging

# # Set up logging to a file
# logging.basicConfig(filename='app.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# # Logging messages
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")
# ===========================================
# Log Rotation
# Log File Creation:

# When you use RotatingFileHandler('app.log', maxBytes=2000, backupCount=5), it starts by logging to the app.log file.
# Initially, this file is created(if it doesn't exist) and logs are written to it.
# When the Log File Reaches the Size Limit(maxBytes=2000):

# If the size of the app.log file exceeds 2000 bytes ( or the maxBytes threshold), it is "rolled over"—which means the current app.log file is archived and a new log file is created.
# By default, the rolled-over file is named something like app.log.1 (the .1 represents the first backup file).
# Backup Files:

# After the first rollover(when the size exceeds 2000 bytes), the original app.log file is archived as app.log.1 and a new app.log file is created for future logging.
# The backupCount = 5 means that a maximum of 5 backup log files will be kept. After 5 backups are created, the oldest log file will be deleted to make space for the newest one.
# The backup files are named sequentially(e.g., app.log.1, app.log.2, etc.). When a new file is rolled over, the existing backup files are renamed(e.g., app.log.1 becomes app.log.2, app.log.2 becomes app.log.3, and so on).
# Rolling Over and Deleting Old Logs:

# Once the file exceeds the size limit(2000 bytes), the log files will rotate. This means the old app.log gets renamed to app.log.1, and a new app.log starts fresh.
# If there are already 5 backup files(app.log.1 through app.log.5), the oldest file(e.g., app.log.5) will be deleted, and the new backup will take its place(i.e., app.log.1 will become app.log.2, and so on).

# from logging.handlers import RotatingFileHandler
# import logging

# # Set up rotating file handler
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# handler.setFormatter(logging.Formatter(
#     '%(asctime)s - %(levelname)s - %(message)s'))

# # Set up logging
# logging.basicConfig(level=logging.DEBUG, handlers=[handler])

# # Log messages
# logging.debug("Debug message")
# logging.info("Info message")
# logging.warning("Warning message")
# ==========================
# import logging
# from logging.handlers import RotatingFileHandler
# from datetime import datetime

# # Generate a dynamic filename based on the current date and time
# log_filename = datetime.now().strftime('app_%Y-%m-%d_%H-%M-%S.log')

# # Set up rotating log handler with the dynamic filename
# handler = RotatingFileHandler(log_filename, maxBytes=2000, backupCount=5)
# handler.setFormatter(logging.Formatter(
#     '%(asctime)s - %(levelname)s - %(message)s'))

# # Set up logging
# logging.basicConfig(level=logging.DEBUG, handlers=[handler])

# # Generate logs (for demonstration, we log a lot of messages to exceed maxBytes)
# for i in range(1000):
#     logging.debug(f"This is debug message {i}")
# ======================
# import logging
# from logging.handlers import RotatingFileHandler
# from datetime import datetime
# import os

# # Get the current working directory
# current_directory = os.getcwd()
# print(current_directory)

# # Generate a dynamic filename based on the current date and time in the current directory
# log_filename = os.path.join(
#     current_directory, datetime.now().strftime('app_%Y-%m-%d_%H-%M-%S.log'))

# # Set up rotating log handler with the dynamic filename
# handler = RotatingFileHandler(log_filename, maxBytes=2000, backupCount=5)
# handler.setFormatter(logging.Formatter(
#     '%(asctime)s - %(levelname)s - %(message)s'))

# # Set up logging
# logging.basicConfig(level=logging.DEBUG, handlers=[handler])

# # Generate logs (for demonstration, we log a lot of messages to exceed maxBytes)
# for i in range(1000):
#     logging.debug(f"This is debug message {i}")
# ====================================
# Create a logfile in a directory


import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
import logging


# Specify the directory where the log file should be created
# Change this to the desired directory
log_directory = 'log'

# Ensure the directory exists
if not os.path.exists(log_directory):
    os.makedirs(log_directory)  # Create the directory if it doesn't exist

# Generate a dynamic filename based on the current date and time
log_filename = os.path.join(
    log_directory, datetime.now().strftime('app_%Y-%m-%d_%H-%M-%S.log'))

# Set up rotating log handler with the dynamic filename
handler = RotatingFileHandler(log_filename, maxBytes=2000, backupCount=5)
handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'))

# Set up logging
logging.basicConfig(level=logging.DEBUG, handlers=[handler])

# Generate logs (for demonstration, we log a lot of messages to exceed maxBytes)
for i in range(1000):
    logging.debug(f"This is debug message {i}")
