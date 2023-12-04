#!/usr/bin/python3
"""module"""
BaseGeometry = __import__("7-base_geometry.py").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
       """Initilize rectangle method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height 

    def area(self):
        """area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
