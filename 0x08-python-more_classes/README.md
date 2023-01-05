# Python - More Classes and Objects

### __doc__
In Python, the __doc__ attribute is a special attribute of a module, class, or function that holds the docstring associated with that object. A docstring is a string literal that appears immediately after the definition of a class, method, function, or module. Docstrings are used to document the purpose and behavior of objects in your code, and can be accessed using the __doc__ attribute.

example of code:
```
def my_function(arg1, arg2):
    """This function does something useful.

    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.

    Returns:
        bool: True if successful, False otherwise.
    """
    # function code goes here
    return True

print(my_function.__doc__)
```

### __repr__
In Python, the __repr__ method is a special method that is used to specify a string representation of an object. This representation is used to display the object in a more user-friendly way when it is printed, or when it is displayed in the interactive interpreter.

The __repr__ method is defined in the object's class and is called when the repr() function is applied to an instance of the object. The repr() function is used to generate a string representation of an object that is as close to the source code form as possible, so that when the string is evaluated using the eval() function, it will produce an object that is equivalent to the original.

example of code:
```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

p = Point(1, 2)
print(p)  # Output: Point(1, 2)
```
In this example, the Point class has a __repr__ method that returns a string representation of the object in the form Point(x, y), where x and y are the values of the x and y attributes of the object. When the print function is called on an instance of the Point class, the __repr__ method is called to generate a string representation of the object, which is then printed to the console.

It is generally a good idea to define a __repr__ method for your classes, as it can make it easier to debug and understand your code. It is also possible to define a __str__ method, which is similar to __repr__, but is used when the str() function is applied to an object. The __str__ method should return a more user-friendly string representation of the object, while the __repr__ method should return a more developer-friendly representation.

### __init__
In Python, the __init__ method is a special method that is called when an instance of a class is created. It is used to initialize the attributes of the instance and perform any other necessary setup.

The __init__ method is defined in the class definition and takes the self parameter, which is a reference to the instance being created. Additional parameters can be added to the __init__ method to accept any necessary information that is required to initialize the instance.

Here is an example of how the __init__ method can be used:
```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(p.x)  # Output: 1
print(p.y)  # Output: 2
```
In this example, the Point class has an __init__ method that initializes the x and y attributes of the instance with the values of the x and y parameters. When an instance of the Point class is created, the __init__ method is called to initialize the instance, and the values of the x and y attributes are set to the values of the x and y parameters.

The __init__ method is called automatically when an instance of the class is created, so you do not need to call it directly. It is an important method to define in your classes, as it allows you to set up the instance correctly and ensure that it is in a valid state when it is created.

### __del__
In Python, the __del__ method is a special method that is called when an object is about to be garbage collected. It is defined in the object's class and can be used to perform any necessary cleanup operations, such as closing open files or releasing resources.

The __del__ method is called automatically by the Python garbage collector when an object is no longer being used and is about to be removed from memory. It is not guaranteed to be called, however, as the garbage collector is free to discard objects at any time.

Here is an example of how the __del__ method can be used:
```
class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = open(self.filename, self.mode)

    def __del__(self):
        self.file.close()

f = File('test.txt', 'w')
# do something with the file
del f  # file is closed when the File object is deleted
```
### __str__
In Python, the __str__ method is a special method that is used to specify a string representation of an object. This representation is used when the str() function is applied to an instance of the object, and it is also used when the object is printed using the print() function.

The __str__ method is defined in the object's class and should return a string representation of the object that is suitable for printing or display to the user. It is generally used to return a more user-friendly string representation of the object, as opposed to the __repr__ method, which should return a more developer-friendly representation.

Here is an example of how the __str__ method can be used:
```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

p = Point(1, 2)
print(p)  # Output: (1, 2)
```
In this example, the Point class has an __init__ method that initializes the x and y attributes of the instance, and a __str__ method that returns a string representation of the object in the form (x, y), where x and y are the values of the x and y attributes of the object. When the print function is called on an instance of the Point class, the __str__ method is called to generate a string representation of the object, which is then printed to the console.

It is generally a good idea to define a __str__ method for your classes, as it can make it easier to understand and debug your code. It is also possible to define a __repr__ method, which is similar to __str__, but is used to generate a more developer-friendly string representation of the object.
