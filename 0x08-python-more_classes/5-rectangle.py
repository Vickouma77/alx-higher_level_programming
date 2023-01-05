#!/usr/bin/python3
"""Define a class rectangle."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Define a new rectangle.
        Args:
            width (int): width of the rectangle.
                        height (int): height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the current width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the current height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the current area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the current perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ __str__ method to print the Rectangle """
        result = ""
        if self.height == 0 or self.width == 0:
            return (result)
        for x in range(self.height):
            for y in range(self.width):
                result += "#"
            result += "\n"
        result = result[0:-1]
        return (result)

    def __repr__(self):
        """ repr method to recreate the Rectangle """
        return ("Rectangle(" + str(self.width) + ", " + str(self.height) + ")")

    def __del__(self):
        """ __del__ method print a message when an instance is deleted """
        print("Bye rectangle...")
