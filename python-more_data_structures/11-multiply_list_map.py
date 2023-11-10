#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    return lambda my_list : my_list * number
my_list = [1, 2, 3, 4, 6]
mymutiply =  mutiply_list_map(my_list, 4)
print(mymutiply(4))
