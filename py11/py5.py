from numpy import *
#Aliasing the array
a=array([10,20,30,40,50])
print(a)

b=a         #assignment copy
print(b)

a[0]=99
print(a)
print(b)
#
print(a)
b=a.view()      #shallow copy

b[0]=100
print(b)
print(a)
#
b=a.copy()  #deep copy
print(b)

a[0]=66
print(a)

print(b)
b[0]=55
print(b)

# print(a)