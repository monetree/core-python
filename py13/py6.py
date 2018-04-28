#accept two matrix from key board and display their product matrix
from numpy import *
r,c=[int(x) for x in input("enter the rows and cols: ").split(",")]
arr1=zeros((r,c))
arr2=zeros((r,c))
print("enter elements: ")
for i in range(r):
	lst=[float(x) for x in input().split()]
	arr1[i]=lst
print("enter elements: ")
for j in range(r):
	lst=[float(y) for y in input().split()]
	arr2[j]=lst
m=matrix(arr1)
n=matrix(arr2)
mul=arr1*arr2
print("arr1")
print(m)
print('a2rr2')
print(n)
print("multiplication")
print(mul)

