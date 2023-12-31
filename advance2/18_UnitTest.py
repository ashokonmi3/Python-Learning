#     "#Method                   Checks that\n",
#     "assertEqual(a, b)          a == b\n",
#     "assertNotEqual(a, b)       a != b\n",
#     "assertTrue(x)              bool(x) is True\n",
#     "assertFalse(x)             bool(x) is False\n",
#     "assertIs(a, b)             a is b\n",
#     "assertIsNot(a, b)          a is not b\n",
#     "assertIsNone(x)            x is None\n",
#     "assertIsNotNone(x)         x is not None\n",
#     "assertIn(a, b)             a in b\n",
#     "assertNotIn(a, b)          a not in b\n",
#     "assertIsInstance(a, b)     isinstance(a, b)\n",
#     "assertNotIsInstance(a, b)  not isinstance(a, b)\n"
#
#     "# Method                   Checks that\n",
#     "* assertEqual(a, b)          a == b\n",
#     "* assertNotEqual(a, b)       a != b\n",
#     "* assertTrue(x)              bool(x) is True\n",
#     "* assertFalse(x)             bool(x) is False\n",
#     "* assertIs(a, b)             a is b\n",
#     "* assertIsNot(a, b)          a is not b\n",
#     "* assertIsNone(x)            x is None\n",
#     "* assertIsNotNone(x)         x is not None\n",
#     "* assertIn(a, b)             a in b\n",
#     "* assertNotIn(a, b)          a not in b\n",
#     "* assertIsInstance(a, b)     isinstance(a, b)\n",
#     "* assertNotIsInstance(a, b)  not isinstance(a, b)\n"



import unittest
a=10
b=20
assertEqual(a,b)


#     "b=20\n",
#     "assertEqual(a,b)"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "def add(x,y):\n",
#     "   return x + y\n",
#     "\n",
#     "x=add(10,15)\n",
#     "if x==25:\n",
#     "    print(\"function is working fine\")\n",
#     "else:\n",
#     "    print(\"function is not working fine\")\n",
#     "x=add(-1,-1)\n",
#     "if x==-2:\n",
#     "    print(\"function is working fine\")\n",
#     "else:\n",
#     "    print(\"function is not working fine\")"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "# import unittest\n",
#     "# # from mod import *\n",
#     "# def funcAdd(x,y):\n",
#     "#    return x + y\n",
#     "\n",
#     "# class SimpleTest(unittest.TestCase):\n",
#     "#    def testadd1(self):\n",
#     "#       self.assertEqual(funcAdd(4,5),9)\n",
#     "#    def testadd2(self):\n",
#     "#        self.assertEqual(funcAdd(4,5),19)\n",
#     "#    def testadd3(self):\n",
#     "#        self.assertEqual(funcAdd(40,5),45)\n",
#     "# if __name__ == '__main__':\n",
#     "#     unittest.main(argv=['first-arg-is-ignored'], exit=False)"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "import unittest\n",
#     "class simpleTest2(unittest.TestCase):\n",
#     "   def setUp(self):\n",
#     "      self.a = 10\n",
#     "      self.b = 20\n",
#     "      print ('\\n start of test')\n",
#     "\n",
#     "   def tearDown(self):\n",
#     "      print ('\\nend of test')\n",
#     "   def testadd(self):\n",
#     "      result = self.a+self.b\n",
#     "      self.assertTrue(result == 30)\n",
#     "        \n",
#     "   def testsub(self):\n",
#     "      result = self.a-self.b\n",
#     "      self.assertTrue(result == -10)\n",
#     "if __name__ == '__main__':\n",
#     "       unittest.main(argv=['first-arg-is-ignored'], exit=False)"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {
#     "scrolled": true
#    },
#    "outputs": [],
#    "source": [
#     "import unittest\n",
#     "class simpleTest2(unittest.TestCase):\n",
#     "   def setUp(self):\n",
#     "      self.a = 10\n",
#     "      self.b = 20\n",
#     "      name = self.shortDescription()\n",
#     "      if name == \"Add\":\n",
#     "         self.a = 10\n",
#     "         self.b = 20\n",
#     "         print (name, self.a, self.b)\n",
#     "      if name == \"sub\":\n",
#     "         self.a = 50\n",
#     "         self.b = 60\n",
#     "         print (name, self.a, self.b)\n",
#     "   def tearDown(self):\n",
#     "      print ('\\nend of test')\n",
#     "   def testadd(self):\n",
#     "      \"\"\"Add\"\"\"\n",
#     "      result = self.a+self.b\n",
#     "      print(result)\n",
#     "      self.assertTrue(result == 30)\n",
#     "   def testsub(self):\n",
#     "      \"\"\"sub\"\"\"\n",
#     "      result = self.a-self.b\n",
#     "      print(result)\n",
#     "\n",
#     "      self.assertTrue(result == -10)\n",
#     "if __name__ == '__main__':\n",
#     "       unittest.main(argv=['first-arg-is-ignored'], exit=False)"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "# setUpClass()\n",
#     "\n",
#     "A class method called before tests in an individual class run.\n",
#     "tearDownClass()\n",
#     "A class method called after tests in an individual class have run.\n",
#     "@classmethod means: when this method is called, we pass the class as the first argument instead of \n",
#     "the instance of that class (as we normally do with methods). \n",
#     "This means you can use the class and its properties inside that method rather than a particular instance.\n",
#     "\n"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "import unittest\n",
#     "class TestFixtures(unittest.TestCase):\n",
#     "   def setUp(self):\n",
#     "      self.a = 10\n",
#     "      self.b = 20\n",
#     "      name = self.shortDescription()\n",
#     "      print ('\\n',name)\n",
#     "   def tearDown(self):\n",
#     "      print ('\\nend of test',self.shortDescription())\n",
#     "   def test1(self):\n",
#     "      \"\"\"One\"\"\"\n",
#     "      result = self.a+self.b\n",
#     "      self.assertTrue(result == 30)\n",
#     "   def test2(self):\n",
#     "      \"\"\"Two\"\"\"\n",
#     "      result = self.a-self.b\n",
#     "      self.assertTrue(result == -100)\n",
#     "if __name__ == '__main__':\n",
#     "    unittest.main(argv=['first-arg-is-ignored'], exit=False)\n"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 1,
#    "metadata": {},
#    "outputs": [
#     {
#      "name": "stderr",
#      "output_type": "stream",
#      "text": [
#       "Fsxs\n",
#       "======================================================================\n",
#       "FAIL: testadd (__main__.suiteTest)\n",
#       "Add\n",
#       "----------------------------------------------------------------------\n",
#       "Traceback (most recent call last):\n",
#       "  File \"<ipython-input-1-27948eba044e>\", line 9, in testadd\n",
#       "    self.assertEqual(result,100)\n",
#       "AssertionError: 90 != 100\n",
#       "\n",
#       "----------------------------------------------------------------------\n",
#       "Ran 4 tests in 0.008s\n",
#       "\n",
#       "FAILED (failures=1, skipped=2, expected failures=1)\n"
#      ]
#     }
#    ],
#    "source": [
#     "import unittest\n",
#     "class suiteTest(unittest.TestCase):\n",
#     "   a = 50\n",
#     "   b = 40\n",
#     "   \n",
#     "   def testadd(self):\n",
#     "      \"\"\"Add\"\"\"\n",
#     "      result = self.a+self.b\n",
#     "      self.assertEqual(result,100)\n",
#     "\n",
#     "   @unittest.skipIf(a>b, \"Skip over this routine\")\n",
#     "   def testsub(self):\n",
#     "      \"\"\"sub\"\"\"\n",
#     "      result = self.a-self.b\n",
#     "      self.assertTrue(result == -10)\n",
#     "  \n",
#     "   @unittest.skipUnless(b == 0, \"Skip over this routine\")\n",
#     "   def testdiv(self):\n",
#     "      \"\"\"div\"\"\"\n",
#     "      result = self.a/self.b\n",
#     "      self.assertTrue(result == 1)\n",
#     "\n",
#     "   @unittest.expectedFailure\n",
#     "   def testmul(self):\n",
#     "      \"\"\"mul\"\"\"\n",
#     "      result = self.a*self.b\n",
#     "      self.assertEqual(result == 0)\n",
#     "\n",
#     "if __name__ == '__main__':\n",
#     "    unittest.main(argv=['first-arg-is-ignored'], exit=False)\n"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 1,
#    "metadata": {},
#    "outputs": [
#     {
#      "name": "stderr",
#      "output_type": "stream",
#      "text": [
#       ".\n",
#       "----------------------------------------------------------------------\n",
#       "Ran 1 test in 0.004s\n",
#       "\n",
#       "OK\n"
#      ]
#     }
#    ],
#    "source": [
#     "import unittest\n",
#     "class SomeTest(unittest.TestCase):\n",
#     "    def setUp(self):\n",
#     "#         super(SomeTest, self).setUp()\n",
#     "        self.mock_data = [1,2,3,4,5]\n",
#     "    def test(self):\n",
#     "        self.assertEqual(len(self.mock_data), 5)\n",
#     "    def tearDown(self):\n",
#     "#         super(SomeTest, self).tearDown()\n",
#     "        self.mock_data = []\n",
#     "if __name__ == '__main__':\n",
#     "    unittest.main(argv=['first-arg-is-ignored'], exit=False)\n"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 1,
#    "metadata": {},
#    "outputs": [
#     {
#      "name": "stderr",
#      "output_type": "stream",
#      "text": [
#       ".\n",
#       "----------------------------------------------------------------------\n",
#       "Ran 1 test in 0.005s\n",
#       "\n",
#       "OK\n"
#      ]
#     }
#    ],
#    "source": [
#     "import unittest\n",
#     "def division_function(dividend, divisor):\n",
#     "    return dividend / divisor\n",
#     "\n",
#     "class MyTestCase(unittest.TestCase):\n",
#     "    def test_using_context_manager(self):\n",
#     "        with self.assertRaises(ZeroDivisionError):\n",
#     "            x = division_function(1, 0)\n",
#     "if __name__ == '__main__':\n",
#     "    unittest.main(argv=['first-arg-is-ignored'], exit=False)"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 2,
#    "metadata": {},
#    "outputs": [
#     {
#      "name": "stderr",
#      "output_type": "stream",
#      "text": [
#       "F..\n",
#       "======================================================================\n",
#       "FAIL: test_correct_input (__main__.ExceptionTestCase)\n",
#       "----------------------------------------------------------------------\n",
#       "Traceback (most recent call last):\n",
#       "  File \"<ipython-input-2-5ba7ef5bc04c>\", line 6, in convert2number\n",
#       "    my_input = int(random_input)\n",
#       "ValueError: invalid literal for int() with base 10: '5jj6'\n",
#       "\n",
#       "During handling of the above exception, another exception occurred:\n",
#       "\n",
#       "Traceback (most recent call last):\n",
#       "  File \"<ipython-input-2-5ba7ef5bc04c>\", line 15, in test_correct_input\n",
#       "    result = convert2number(\"5jj6\")\n",
#       "WrongInputException\n",
#       "\n",
#       "During handling of the above exception, another exception occurred:\n",
#       "\n",
#       "Traceback (most recent call last):\n",
#       "  File \"<ipython-input-2-5ba7ef5bc04c>\", line 18, in test_correct_input\n",
#       "    self.fail()\n",
#       "AssertionError: None\n",
#       "\n",
#       "----------------------------------------------------------------------\n",
#       "Ran 3 tests in 0.003s\n",
#       "\n",
#       "FAILED (failures=1)\n"
#      ]
#     }
#    ],
#    "source": [
#     "import unittest\n",
#     "class WrongInputException(Exception):\n",
#     "    pass\n",
#     "def convert2number(random_input):\n",
#     "    try:\n",
#     "        my_input = int(random_input)\n",
#     "        return my_input\n",
#     "    except ValueError:\n",
#     "        raise WrongInputException\n",
#     "class ExceptionTestCase(unittest.TestCase):\n",
#     "    def test_wrong_input_string(self):\n",
#     "        self.assertRaises(WrongInputException, convert2number, \"not a number\")\n",
#     "    def test_correct_input(self):\n",
#     "        try:\n",
#     "            result = convert2number(\"5jj6\")\n",
#     "            self.assertIsInstance(result, int)\n",
#     "        except WrongInputException:\n",
#     "            self.fail()\n",
#     "if __name__ == '__main__':\n",
#     "    unittest.main(argv=['first-arg-is-ignored'], exit=False)"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 5,
#    "metadata": {},
#    "outputs": [
#     {
#      "name": "stderr",
#      "output_type": "stream",
#      "text": [
#       "F..Es.\n",
#       "======================================================================\n",
#       "ERROR: test_maybe_skipped (__main__.MyTestCase)\n",
#       "----------------------------------------------------------------------\n",
#       "Traceback (most recent call last):\n",
#       "  File \"<ipython-input-5-c4570b7602de>\", line 21, in test_maybe_skipped\n",
#       "    if not external_resource_available():\n",
#       "NameError: name 'external_resource_available' is not defined\n",
#       "\n",
#       "======================================================================\n",
#       "FAIL: test_correct_input (__main__.ExceptionTestCase)\n",
#       "----------------------------------------------------------------------\n",
#       "Traceback (most recent call last):\n",
#       "  File \"<ipython-input-2-5ba7ef5bc04c>\", line 6, in convert2number\n",
#       "    my_input = int(random_input)\n",
#       "ValueError: invalid literal for int() with base 10: '5jj6'\n",
#       "\n",
#       "During handling of the above exception, another exception occurred:\n",
#       "\n",
#       "Traceback (most recent call last):\n",
#       "  File \"<ipython-input-2-5ba7ef5bc04c>\", line 15, in test_correct_input\n",
#       "    result = convert2number(\"5jj6\")\n",
#       "WrongInputException\n",
#       "\n",
#       "During handling of the above exception, another exception occurred:\n",
#       "\n",
#       "Traceback (most recent call last):\n",
#       "  File \"<ipython-input-2-5ba7ef5bc04c>\", line 18, in test_correct_input\n",
#       "    self.fail()\n",
#       "AssertionError: None\n",
#       "\n",
#       "----------------------------------------------------------------------\n",
#       "Ran 6 tests in 0.006s\n",
#       "\n",
#       "FAILED (failures=1, errors=1, skipped=1)\n"
#      ]
#     }
#    ],
#    "source": [
#     "import unittest,sys\n",
#     "\n",
#     "class MyTestCase(unittest.TestCase):\n",
#     "\n",
#     "    @unittest.skip(\"demonstrating skipping\")\n",
#     "    def test_nothing(self):\n",
#     "        self.fail(\"shouldn't happen\")\n",
#     "\n",
#     "#     @unittest.skipIf(mylib.__version__ < (1, 3),\n",
#     "#                      \"not supported in this library version\")\n",
#     "    def test_format(self):\n",
#     "        # Tests that work for only a certain version of the library.\n",
#     "        pass\n",
#     "\n",
#     "    @unittest.skipUnless(sys.platform.startswith(\"win\"), \"requires Windows\")\n",
#     "    def test_windows_support(self):\n",
#     "        # windows specific testing code\n",
#     "        pass\n",
#     "\n",
#     "    def test_maybe_skipped(self):\n",
#     "        if not external_resource_available():\n",
#     "            self.skipTest(\"external resource not available\")\n",
#     "        # test code that depends on the external resource\n",
#     "        pass\n",
#     "if __name__ == '__main__':\n",
#     "    unittest.main(argv=['first-arg-is-ignored'], exit=False)"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 1,
#    "metadata": {},
#    "outputs": [
#     {
#      "name": "stderr",
#      "output_type": "stream",
#      "text": [
#       ".F\n",
#       "======================================================================\n",
#       "FAIL: test_02_search_by_name (__main__.PythonOrgSearch)\n",
#       "----------------------------------------------------------------------\n",
#       "Traceback (most recent call last):\n",
#       "  File \"<ipython-input-1-c5e255b8bff9>\", line 36, in test_02_search_by_name\n",
#       "    assert \"No results found.\" not in driver.page_source\n",
#       "AssertionError\n",
#       "\n",
#       "----------------------------------------------------------------------\n",
#       "Ran 2 tests in 34.336s\n",
#       "\n",
#       "FAILED (failures=1)\n"
#      ]
#     }
#    ],
#    "source": [
#     "import unittest\n",
#     "from time import sleep\n",
#     "from selenium import webdriver\n",
#     "from selenium.webdriver.common.keys import Keys\n",
#     "\n",
#     "class PythonOrgSearch(unittest.TestCase):\n",
#     "    \n",
#     "    def setUp(self):\n",
#     "        self.driver = webdriver.Chrome()\n",
#     "        # self.driver.maximize_window()\n",
#     "\n",
#     "    \n",
#     "    def test_01_search_in_python_org(self):\n",
#     "        driver = self.driver\n",
#     "        driver.get(\"http://www.python.org\")\n",
#     "        #self.assertIn(\"Python\", driver.title)\n",
#     "        assert \"Python\" in driver.title\n",
#     "        elem = driver.find_element_by_name(\"q\")\n",
#     "        elem.send_keys(\"python\")\n",
#     "        sleep(5)\n",
#     "        elem.send_keys(Keys.RETURN)\n",
#     "        sleep(5)\n",
#     "        assert \"No results found.\" not in driver.page_source\n",
#     "#         self.driver.quit()\n",
#     "\n",
#     "    \n",
#     "    def test_02_search_by_name(self):\n",
#     "        driver = self.driver\n",
#     "        driver.get(\"http://www.python.org\")\n",
#     "        sleep(5)\n",
#     "        elem = driver.find_element_by_name(\"q\")\n",
#     "        elem.send_keys(\"qython\")\n",
#     "        sleep(5)\n",
#     "        elem.send_keys(Keys.RETURN)\n",
#     "        sleep(5)\n",
#     "        assert \"No results found.\" not in driver.page_source\n",
#     "#         self.driver.quit()\n",
#     "\n",
#     "        # get the search textbox\n",
#     "        # self.search_field = self.driver.find_element_by_name(\"q\")\n",
#     "        # # enter search keyword and submit\n",
#     "        # self.search_field.send_keys(\"Python class\")\n",
#     "        # self.search_field.submit()\n",
#     "        # #get the list of elements which are displayed after the search\n",
#     "        #currently on result page using find_elements_by_class_name method\n",
#     "        # list_new = self.driver.find_elements_by_class_name(\"r\")\n",
#     "        # self.assertEqual(10, len(list_new))\n",
#     "     \n",
#     "    def tear_down(self):\n",
#     "        self.driver.quit()\n",
#     "\n",
#     "\n",
#     "\n",
#     "if __name__ == '__main__':\n",
#     "    unittest.main(argv=['first-arg-is-ignored'], exit=False)"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {},
#    "outputs": [],
#    "source": []
#   }
#  ],
#  "metadata": {
#   "kernelspec": {
#    "display_name": "Python 3",
#    "language": "python",
#    "name": "python3"
#   },
#   "language_info": {
#    "codemirror_mode": {
#     "name": "ipython",
#     "version": 3
#    },
#    "file_extension": ".py",
#    "mimetype": "text/x-python",
#    "name": "python",
#    "nbconvert_exporter": "python",
#    "pygments_lexer": "ipython3",
#    "version": "3.7.3"
#   }
#  },
#  "nbformat": 4,
#  "nbformat_minor": 2
# }