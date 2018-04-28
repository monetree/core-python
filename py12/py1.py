#indexing and slicing possible on 1d and 2d array repeat not possible
from numpy import *
# arr=array([30,20,-20,10,55,66])
# print(arr)
#
# print(arr[0])
# print(arr[4])
# print(arr[1:3])
# print(arr[1:6:2])
# print(arr[5:0:-1])
# print(arr[5:0:-2])
# print(arr[5::-1])
# print(arr*2)
# repetation is not possible in array so it it
# works as multiplication on each elements

arr=array([50,30,22,-1,14])
# print(arr)
# print(arr.ndim) # returns which kind of dimensional array

arr2=array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2)
# print(arr2.ndim)

# print(arr)
# print(arr.shape) #returns size of array(index)
#
# print(arr2.shape)

arr3=array([[1,2,3],[4,5,6]])
# print(arr3)
# print(arr3.shape)
# arr3.shape=(3,2)
# print(arr3)

# print(arr)
# print(arr.size)
# print(arr2.size)
# print(arr3.size)

# print(arr.itemsize)
# print(arr2.itemsize)
# print(arr3.itemsize)

# print(arr)
print(arr.nbytes)

arr4=array([1.2,3.2,4.5])
print(arr4.nbytes)
#
print(arr.dtype)
print(arr4.dtype)