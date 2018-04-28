'''
map() function is similar to filter() function but it acts on each
element of the sequence and perhaps changes the element
syn:map(lambda,sequence)

'''
#creates a lambda that returns squares of all elements in a list

lst=[2,3,4,5,6,-3]
obj=map(lambda x:x*x,lst)
for i in obj:print(i)

'''
lst1=list(obj)
print(lst1)
'''
