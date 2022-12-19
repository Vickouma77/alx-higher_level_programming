##  Python - Exceptions

Exceptions are a mechanism in Python that allows you to handle errors or unusual 
conditions in your code. When an error occurs, Python raises an exception, which can be
caught and handled using a try/except block.
##### Here is an example of how you can use a try/except
```
try:
    # Some code that might raise an exception
    x = 1 / 0
except ZeroDivisionError:
    # Code to handle the ZeroDivisionError exception
    print("You can't divide by zero!")

```
