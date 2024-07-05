
Exercise 1
Tests for the map_longest() function are implemented in a file named exercise.py. The implementation of this function should be in a file named solution.py. Your task is to complete the implementation of this function in solution.py so that it passes the tests implemented in exercise.py.



How map_longest() works:

The function takes a list of words (no validation) and returns the length of the longest word in a list. If an empty list is passed, it returns 0.



Example:



[IN]: map_longest(['python', 'sql'])
[OUT]: 6


[IN]: map_longest(['java', 'sql', 'r'])
[OUT]: 4


Solution 1

Solution I:

def map_longest(words):
    if not words:
        return 0
    lengths = []
    for word in words:
        lengths.append(len(word))
    return max(lengths)


Solution II:

def map_longest(words):
    return max(len(word) for word in words) if words else 0


==================================================================================
Exercise 2
Tests for the filter_ge_four_char() function are implemented in a file named exercise.py. The implementation of this function should be in a file named solution.py. Your task is to complete the implementation of this function in solution.py so that it passes the tests implemented in exercise.py.



How filter_ge_four_char() works:

The function takes a list of words (no validation) and returns a list of words that are exactly four characters or more.



Example:



[IN]: filter_ge_four_char(['programm', 'python', 'sql'])
[OUT]: ['programm', 'python']


[IN]: filter_ge_four_char(['c++', 'sql'])
[OUT]: []


Solution 2

Solution I:

def filter_ge_four_char(words):
    result = []
    for word in words:
        if len(word) >= 4:
            result.append(word)
    return result


Solution II:

def filter_ge_four_char(words):
    return [word for word in words if len(word) >= 4]

==================================================================================

Exercise 3
Tests for the factorial() function are implemented in a file named exercise.py. The implementation of this function should be in a file named solution.py. Your task is to complete the implementation of this function in solution.py so that it passes the tests implemented in exercise.py.



How factorial() works:

The function takes a non-negative integer and returns the factorial of that number. You do not need to implement validation of the argument passed to the function.



Tip: Use recursion.



Example:



[IN]: factorial(6)
[OUT]: 720


[IN]: factorial(10)
[OUT]: 3628800

Solution 3

Solution I:

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


Solution II:

from functools import reduce
import operator
 
 
def factorial(n):
    return reduce(operator.mul, range(1, n+1), 1)

==================================================================================
Exercise 4
Tests for the count_string() function are implemented in a file named exercise.py. The implementation of this function should be in a file named solution.py. Your task is to complete the implementation of this function in solution.py so that it passes the tests implemented in exercise.py.



How count_string() works:

The function takes a list (without validation) and returns the number of elements of type str present in the list.



Example:



[IN]: count_string(['p', 2, 4.3, None])
[OUT]: 1


[IN]: count_string({'p', 2, 4.3, True, 'True', None})
[OUT]: 2


Solution 4

Solution I:

def count_string(items):
    total = 0
    for item in items:
        if isinstance(item, str):
            total += 1
    return total


Solution II:

def count_string(items):
    return sum(isinstance(item, str) for item in items)


==================================================================================
Exercise 5
Tests for the remove_duplicates() function are implemented in a file named exercise.py. The implementation of this function should be in a file named solution.py. Your task is to complete the implementation of this function in solution.py so that it passes the tests implemented in exercise.py.



How remove_duplicates() works:

The function takes a list (no validation), removes duplicates, and returns the list with no duplicates.



Example:



[IN]: remove_duplicates([1, 5, 3, 2, 2, 4, 2, 4])
[OUT]: [1, 2, 3, 4, 5]


[IN]: remove_duplicates([1, 1, 1, 1])
[OUT]: [1]


Solution 5
def remove_duplicates(items):
    return list(set(items))

==================================================================================

Exercise 6
Tests for the is_distinct() function are implemented in a file named exercise.py. The implementation of this function should be in a file named solution.py. Your task is to complete the implementation of this function in solution.py so that it passes the tests implemented in exercise.py.



How is_distinct() works:

The function takes a list (no validation) and returns True if the list contains no duplicates, returns False otherwise.



Example:



[IN]: is_distinct([1, 2, 3])
[OUT]: True


[IN]: is_distinct([1, 2, 3, 3])
[OUT]: False


Solution 6

Solution I:

def is_distinct(items):
    return len(items) == len(set(items))


Solution II:

from collections import Counter
 
def is_distinct(items):
    counts = Counter(items)
    return all(count == 1 for count in counts.values())

==================================================================================
Exercise 7
Tests for the Phone class are in a file named exercise.py. The implementation of this class should be in a file named solution.py. Your task is to complete the implementation of this class in solution.py so that it passes the tests implemented in exercise.py.

The Phone class should have two user-defined class attributes named appropriately:

brand

model



You can set the values of these attributes freely, e.g.



brand = 'Apple'
model = 'iPhone X'


Solution 7
class Phone:
    brand = 'Apple'
    model = 'iPhone X'

==================================================================================
Exercise 8
Tests for the Laptop class are in a file named exercise.py. The implementation of this class should be in a file named solution.py. Your task is to complete the implementation of this class in solution.py so that it passes the tests implemented in exercise.py.



The Laptop class in the __init__() method should set three instance attributes (without validation) with the names:

brand

model

price

Solution 8
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price



==================================================================================

Exercise 9
Tests for the Laptop class are in a file named exercise.py.

The Laptop class in the __init__() method sets three instance attributes (without validation) with the names:

brand

model

price



Your task is to fix the Laptop implementation in solution.py to pass the tests implemented in exercise.py. Add validation for an instance attribute named price. If the value passed is of type int or float set the value of this attribute, otherwise raise a TypeError.



Solution 9
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        if not isinstance(price, (int, float)):
            raise TypeError(
                'The price attribute must be a positive int or float.'
            )
        self.price = price

==================================================================================
Exercise 10
Tests for the Laptop class are in a file named exercise.py.

The Laptop class in the __init__() method sets three instance attributes with names:

brand

model

price



Your task is to fix the Laptop implementation in solution.py to pass the tests implemented in exercise.py. Add another validation for an instance attribute named price. If the passed value is positive set the value of this attribute, otherwise raise ValueError.

Solution 10
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        if not isinstance(price, (int, float)):
            raise TypeError(
                'The price attribute must be a positive int or float.'
            )
        if not price > 0:
            raise ValueError(
                'The price attribute must be positive.'
            )
        self.price = price


==================================================================================
Exercise 11
Tests for the Laptop class are in a file named exercise.py.

The Laptop class in the __init__() method sets three instance attributes with names:

brand

model

price



Your task is to fix the Laptop implementation in solution.py to pass the tests implemented in exercise.py. Add validation for an instance attribute named brand. If the value passed is an object of type str set the value of this attribute, otherwise raise a TypeError.



Solution 11
class Laptop:
    def __init__(self, brand, model, price):
        if not isinstance(brand, str):
            raise TypeError(
                'The brand attribute must be string.'
            )
        self.brand = brand
        self.model = model
        if not isinstance(price, (int, float)):
            raise TypeError(
                'The price attribute must be a positive int or float.'
            )
        if not price > 0:
            raise ValueError(
                'The price attribute must be positive.'
            )
        self.price = price


==================================================================================

Exercise 12
Tests for the Pet class are in a file named exercise.py. Your task is to fix the Pet implementation in solution.py so that it passes the tests implemented in exercise.py.



Implement a method named name() that returns the value of the protected attribute _name. Then use the @property decorator to create a property with the same name as method (a read-only property).



Solution 12
class Pet:
    def __init__(self, name):
        self._name = name
 
    @property
    def name(self):
        return self._name


==================================================================================
Exercise 13
Tests for the Pet class are in a file named exercise.py. Your task is to fix the Pet implementation in solution.py so that it passes the tests implemented in exercise.py.



Implement a method named age() that returns the value of the protected attribute _age. Then use the @property decorator to create a property with the same name as method (a read-only property).




Solution 13
class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age
 
    @property
    def name(self):
        return self._name
 
    @property
    def age(self):
        return self._age


==================================================================================
Exercise 14
Tests for the Person class are in a file named exercise.py. Your task is to fix the Person implementation in solution.py so that it passes the tests implemented in exercise.py.



Implement a special method named __repr__() that is a formal representation of an object of Person class.



Example:



[IN]: person = Person('John', 'Doe')
[IN]: print(person)
[OUT]: Person(fname='John', lname='Doe')


Solution 14
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
 
    def __repr__(self):
        return f"Person(fname='{self.fname}', lname='{self.lname}')"

==================================================================================
Exercise 15
Tests for the Vector class are in a file named exercise.py. Your task is to fix the Vector implementation in solution.py so that it passes the tests implemented in exercise.py.



Implement a special method named __repr__() that is a formal representation of an object of Vector class.



Example:



[IN]: v1 = Vector(3, 4, 5)
[IN]: print(v1)
[Out]: Vector(3, 4, 5)


Solution 15
class Vector:
    def __init__(self, *components):
        self.components = components
 
    def __repr__(self):
        return f'Vector{self.components}'
    

==================================================================================
Exercise 16
Tests for the Vector class are in a file named exercise.py. Your task is to fix the Vector implementation in solution.py so that it passes the tests implemented in exercise.py.



Implement a special method called __len__() that will return the length of a Vector (number of coordinates).



Example:



[IN]: v1 = Vector(3, 4, 5)
[IN]: print(len(v1))
[Out]: 3


Solution 16
class Vector:
    def __init__(self, *components):
        self.components = components
 
    def __repr__(self):
        return f'Vector{self.components}'
 
    def __len__(self):
        return len(self.components)


==================================================================================