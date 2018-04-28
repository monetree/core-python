#to accept matrix from keyboard and find its transpoze
from numpy import *
# r,c=[int(x) for x in input("enter rows and cols: ").split(",")]
# str=input("enter elements:\n")
# m=matrix(str)
# m=reshape(m,(r,c))
# print("original matrix: \n")
# print(m)
# print('transpose matrix: \n')
# print(m.transpose())

r,c=[int(x) for x in input("enter rows and columns").split(',')]
str=input("enter elements:")
m=matrix(str)
m=reshape(m,(r,c))
print(m)
print(m.transpose())
