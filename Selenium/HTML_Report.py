import unittest
from Test_Suite import PythonOrgSearch
from Test_Suite2 import PythonOrgSearch1
import HTMLTestRunner
import os
 



# get the directory path to output report file
dir = os.getcwd()
# get all tests from SearchText and HomePageTest class
search_text = unittest.TestLoader().loadTestsFromTestCase(PythonOrgSearch)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(PythonOrgSearch1)
 
# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text])

# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary_vipin.html", "w")
 
# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')
# run the suite
# configure HTMLTestRunner options
#runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')

runner.run(test_suite)
 
# get all tests from SearchText and HomePageTest class
# search_text = unittest.TestLoader().loadTestsFr#mTestCase(SearchText)
# home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
 
# # create a test suite combining search_text and home_page_test
# test_suite = unittest.TestSuite([home_page_test, search_text])
 
# # open the report file
# outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")
 
# # configure HTMLTestRunner options
# runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')
 
# # run the suite using HTMLTestRunner
# runner.run(test_suite)