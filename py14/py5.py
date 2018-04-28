'''
a=[4,5,6]
b=[1,5,2.2]
lst=[]
for x in range(len(a)):
    lst.append(a[x]+b[x])
print(lst)
'''
#list compre
a=[4,5,6]
b=[1,5,2.2]
lst=[a[x]+b[x] for x in range(len(a))]
print(lst)
