from numpy import *
arr=arange(10)
print(arr)
arr1=arr.reshape(2,5)
print(arr1)

arr2=arr1.reshape(5,2)
print(arr2)

arr3=arr2.flatten()
print(arr3)