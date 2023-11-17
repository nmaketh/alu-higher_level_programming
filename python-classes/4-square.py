#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must
"""
class Square:
    """ defines the class square"""
    def ___init___(self, size=0):
        """initialise the square"""
        self.__size = size
    @property
    def size(self):
        return self.__size 
    @size.setter
    def size(self, value):
        if isinstance(type(value), int):
            raise TypeError("size must be an integer")
        elif value <0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        return self.__size ** 2

