# Python - Almost a circle
Project done during Full Stack Software Engineering studies at Alx Africa. It aims to learn about unit testing, serialization,deserialization, JSON, ```args``` and ```kwargs``` in python

## Tools
- python scripts are written with python 3.8.5
- Tested on Ubuntu 20.04

## UNIT TEST

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


