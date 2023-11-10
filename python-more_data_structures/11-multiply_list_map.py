#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    return lambda my_list : my_list * number
mymutiply =  mutiply_list_map(my_list, number)
print(mymutiply)
