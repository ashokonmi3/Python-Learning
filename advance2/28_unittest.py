# unittest
# Pytest
# nose
#
# Method                   Checks that
# assertEqual(a, b)          a == b
# assertNotEqual(a, b)       a != b
# assertTrue(x)              bool(x) is True
# assertFalse(x)             bool(x) is False
# assertIs(a, b)             a is b
# assertIsNot(a, b)          a is not b
# assertIsNone(x)            x is None
# assertIsNotNone(x)         x is not None
# assertIn(a, b)             a in b
# assertNotIn(a, b)          a not in b
# assertIsInstance(a, b)     isinstance(a, b)
# assertNotIsInstance(a, b)  not isinstance(a, b)
# #

import unittest


# def add(x, y):
#     return x + y
# #


# class SimpleTest(unittest.TestCase):
#     def testadd1(self):
#         self.assertEqual(add(4, 5), 9)

#     def testadd2(self):
#         self.assertEqual(add(-2, 5), 3)


# if __name__ == '__main__':
#     unittest.main()
# ----------------------

# class simpleTest2(unittest.TestCase):
#     def setUp(self):
#         self.a = 10
#         self.b = 20
#         name = self.shortDescription()
#         if name == "Add":
#             self.a = 10
#             self.b = 20
#             print(name, self.a, self.b)
#         if name == "sub":
#             self.a = 50
#             self.b = 60
#             print(name, self.a, self.b)

#     def tearDown(self):
#         print('\nend of test', self.shortDescription())

#     def testadd(self):
#         """Add"""
#         result = self.a+self.b
#         self.assertTrue(result == 30)

#     def testsub(self):
#         """sub"""
#         result = self.a-self.b
#         self.assertTrue(result == -10)


# if __name__ == '__main__':
#     unittest.main()


# -------------------

# setUpClass()

# A class method called before tests in an individual class run.
# tearDownClass()
# A class method called after tests in an individual class have run.
# @classmethod means: when this method is called, we pass the class as the first argument instead of
# the instance of that class (as we normally do with methods).
# This means you can use the class and its properties inside that method rather than a particular instance.


# class TestFixtures(unittest.TestCase):

#     def setUp(self):
#         self.a = 10
#         self.b = 20
#         name = self.shortDescription()
#         print('\n', name)
#         print("Setup")

#     def tearDown(self):
#         print('\nend of test', self.shortDescription())
#         print("TearDown")

#     def test1(self):
#         """One"""
#         print("Test1")
#         result = self.a+self.b
#         self.assertTrue(result == 30)

#     def test2(self):
#         """Two"""
#         print("Test2")
#         result = self.a-self.b
#         self.assertTrue(result == -10)


# if __name__ == '__main__':
#     unittest.main()

# -----------------

# import unittest


# class SimpleTest(unittest.TestCase):
#     def test1(self):
#         self.assertEqual(4 + 5, 9)

#     def test2(self):
#         self.assertNotEqual(5 * 2, 10)

#     def test3(self):
#         self.assertTrue(4 + 5 == 9, "The result is False")

#     def test4(self):

#         self.assertTrue(4 + 5 == 10, "assertion fails")

#     def test5(self):
#         self.assertIn(3, [1, 2, 3])

#     def test6(self):
#         self.assertNotIn(3, range(5))


# if __name__ == '__main__':
#     unittest.main()


# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('FOO'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])

#     def test_error(self):
#         s = 'hello world python'
#         with self.assertRaises(TypeError):
#             s.split(2)


# if __name__ == '__main__':
#     unittest.main()


# suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
# unittest.TextTestRunner(verbosity=2).run(suite)

# ====================================
# import unittest


# def add(x, y):
#     return x+y


# class SimpleTest(unittest.TestCase):
#     @unittest.skip("demonstrating skipping")
#     def testadd1(self):
#         self.assertEquals(add(4, 5), 9)


# if __name__ == '__main__':
#     unittest.main()
# ===========================================

class suiteTest(unittest.TestCase):
    a = 50
    b = 40

    def testadd(self):
        """Add"""
        result = self.a+self.b
        self.assertEqual(result, 100)

    @unittest.skipIf(a > b, "Skip over this routine")
    def testsub(self):
        """sub"""
        result = self.a-self.b
        self.assertTrue(result == -10)

    @unittest.skipUnless(b == 0, "Skip over this routine")
    def testdiv(self):
        """div"""
        result = self.a/self.b
        self.assertTrue(result == 1)

    @unittest.expectedFailure  # x will be result
    def testmul(self):
        """mul"""
        result = self.a*self.b
        self.assertEqual(result == 0)


if __name__ == '__main__':
    unittest.main()
