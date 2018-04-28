#create o list comprehension to generate even nos from 1 to 10
#normal code
'''
lst = []
for x in range(2, 11,2):
    lst.append(x)
print(lst)
'''
#list comprehension code
lst=[x for x in range(2,11,2)]
print(lst)