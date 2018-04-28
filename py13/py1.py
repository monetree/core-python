from numpy import *
arr=array([[1,2,3],
           [2,4,3],
           [6,0,2]])
# print(arr)
#
m=matrix(arr)
# print(m)
#
# d=diagonal(arr)
# print(d)

# max=m.max()
# print(max)
#
# min=m.min()
# print(min)

# sum=m.sum()
# print(sum)
#
# avg=m.mean()
# print(avg)

# print(sort(m))

print(sort(m,axis=0))

print(m.transpose())
