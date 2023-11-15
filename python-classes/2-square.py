#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """Private instance attribute: size"""
    def __init___(self, size = none):
       self.__size = size
       if not isinstance(self.__size, (int)):
         raise TypeError("size must be an integer")
       if self.__size < 0:
         raise ValueError("size must be >= 0")
