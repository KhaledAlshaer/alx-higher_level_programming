#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, val):
        """sets width value"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @height.setter
    def height(self, val):
        """stes height value"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """returns x"""
        return self.__x

    @x.setter
    def x(self, val):
        """sets x value"""
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """returns y"""
        return self.__y

    @y.setter
    def y(self, val):
        """sets y value"""
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("x must be >= 0")
        self.__y = val

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with # and accounting for x and y"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """returns a string representation of the object"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
