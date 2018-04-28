#list comprehension: creating list from list tuples

#create a list comprehesion to find square of integer from 1 to 10
#normal code
'''
lst=[]
for i in range(1,11):
    lst.append(i*i)
print(lst)
'''
#list comprehension code

lst=[i*i for i in range(1,20)]
print(lst)
