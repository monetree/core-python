#matrix ddition and substrction
from numpy import *
a1=array([[1,2,3],[4,5,6],[7,8,9]])
a2=array([[1,0,0],[2,2,2],[2,-1,-2]])
m1=matrix(a1)
m2=matrix(a2)
m3=m1+m2
print(m3)
m4=m1*m2
print(m4)
m5=m2-m1
print(m5)
