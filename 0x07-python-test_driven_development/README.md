# Python Test Driven Development

Test-driven development (TDD) is a software development process that involves writing tests for a piece of code before writing the code itself. The goal of TDD is to ensure that the code is correct and meets the specified requirements.

In TDD, you start by writing a test that defines the desired behavior of the code. The test should define the input to the code and the expected output. Then, you run the test and see that it fails because the code has not been implemented yet.

Next, you write the code to make the test pass. You run the test again and see that it passes. You can then repeat this process, writing more tests and implementing the code to make the tests pass.:smile:

#### Benefits of TDD
- It helps you write code that is correct and meets the specified requirements
- It helps you identify and fix defects early in the development process
- It helps you design your code in a modular and testable way
- It helps you document your code and its intended behavior

# DOCTEST
doctest is a module in Python that allows you to embed test cases in the documentation of a module, function, or class. The doctest module searches for lines in the documentation that look like interactive Python sessions, and then executes the code and checks the output to see if it matches the expected results.

To use doctest, you need to include test cases in the documentation of your code. The test cases should be written as interactive Python sessions, with the input followed by the expected output. For example:

```
def add(a, b):
    """
    Add two numbers and return the result.

    Examples:
    >>> add(1, 2)
    3
    >>> add(10, 20)
    30
    """
   
    return a + b
```

# UNITTEST
The unittest module is a unit testing framework in Python. It is part of the standard library and provides a way to write and run automated tests for your code.

To use unittest, you need to create a test case class that subclasses unittest.TestCase. Then, you can define one or more methods in the class that start with the word test. These methods will be run by the testing framework when you run the tests.

Here's a simple example of a test case class:

```
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
```
