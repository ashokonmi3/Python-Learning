import logging

# debug > Info > warning > error > critical
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
# x = 10
# logging.debug("hi ", x)


# logging.basicConfig(filename="test.log", level=logging.DEBUG)
# logging.warning("warning message")
# logging.info("info message")
# logging.error("error message")


logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.warning("warning message")
logging.info("info message")
logging.error("error message")
