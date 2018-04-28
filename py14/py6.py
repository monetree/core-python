#wa list comprehension to retrive common elements from two list
'''
a=[1,3,4,9,10,-1]
b=[3,-1,5,6,1,7]
lst=[]
for i in a:
    if i in b:
        lst.append(i)
print(lst)
'''

#list comp code
a=[1,3,4,9,10,-1]
b=[3,-1,5,6,1,7]
lst=[i for i in a if i in b]
print(lst)
