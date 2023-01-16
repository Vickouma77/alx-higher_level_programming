#!/usr/bin/python3
"""Module with class Rectangle which inherits from Base
"""
from models.base import  Base


class Rectangle(Base):
    """class Rectangle which inherits Base properties

     Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
    """

    self.width = width
    self.height = height
    self.x = x
    self.y = y
    super().__init__(id)
