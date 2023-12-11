#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        def width(self):
            """returns the width"""
            return self.__width

        def width(self, val):
            """sets width value"""
            if val != int:
                raise TypeError("width must be an integer")
            if val <= 0:
                raise ValueError("width must be > 0")
            self.__width = val

        def height(self):
            """returns the height"""
            return self.__height

        def height(self, val):
            """stes height value"""
            if val != int:
                raise TypeError("height must be an integer")
            if val <= 0:
                raise ValueError("height must be > 0")
            self.__height = val

        def x(self):
            """returns x"""
            return self.__x

        def x(self, val):
            """sets x value"""
            if x != int:
                raise TypeError("x must be an integer")
            if x < 0:
                raise ValueError("x must be >= 0")
            self.__x = val

        def y(self):
            """returns y"""
            return self.__y

        def y(self, val):
            """sets y value"""
            if y != int:
                raise TypeError("y must be an integer")
            if y < 0:
                raise ValueError("x must be >= 0")
            self.__y = val

        def area(self):
                """returns the area of the rectangle"""
                return self.width * self.height

        def display(self):
                """prints in stdout the Rectangle instance with #"""
