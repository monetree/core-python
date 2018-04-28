'''
reduce() : function reduces a sequence of elements to a single value depending
on a lambda  expression
'''
#create a lambda function to calculate the products of elements of a list
lst=[2,3,4,5,6,-3]
from functools import *
result=reduce(lambda x,y:x*y, lst)
print(result)
