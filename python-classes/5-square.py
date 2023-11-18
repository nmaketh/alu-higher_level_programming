#!/usr/bin/python3
'''defines class square'''


class Square:
    '''class square'''
    def __init__(self, size=0):
        '''initializes the square '''
        self.size = size 
    @property
    def size(self):
        '''getting size'''
        return self.___size
    @size.setter
    def size(self, value):
        '''setting the size'''
        if not isinstance(value, int):
           return TypeError("size must be an integer")
        elif value < 0:
           return ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        '''defines area of square'''
        self.__size*self.__size

    def my_print(self):
        ''' printing the character "#"'''
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
           print("")
