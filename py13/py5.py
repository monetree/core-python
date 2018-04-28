# #to accept matrix from keyboard  -v2.0
# from numpy import *
# r,c=[int(x) for x in input("enter rows and cols: ").split(",")]
# arr=zeros((r,c))
# print("enter elements: ")
# for i in range(r):
#     lst=[float(x) for x in input().split()]
#     arr[i]=lst
# m=matrix(arr)
# print("original matrix")
# print(m)
# print('transpose')
# print(m.transpose())
#

from numpy import *
r,c=[int(x) for x in input('enter nos: ').split(',')]
arr = zeros((r,c))
for i in range(r):
    lst=[float(x) for x in input('enter again').split()]
    arr[i]=lst
m=matrix(arr)

print(m.transpose())