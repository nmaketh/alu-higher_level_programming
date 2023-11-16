#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """Private instance attribute: size"""
    
    def __init___(self, size=0):
       """ initializes size.
       arg:

           size(int): the size of the new square.
           """
       if size != int:
         raise TypeError("size must be an integer")
       elif size < 0:
          raise ValueError("size must be >= 0")
       self.__size = size
