'''
filter(): function is is useful to filter the elements of a
sequence depending on the result of a function
syn:filter(lambda,sequence)

'''
#create a lambda that returns even numbers from a list of numbers
#to filter out evens from a list

# lst=[4,5,6,7,8,9,10]
# res=filter(lambda x:x%2==0,lst)
# for i in res:print(i)


#filter only positive nos from a group of numbers

# lst=[4,-5,-6,8,-9,-2,12]
# res=filter(lambda x:x>0,lst)
# for i in res:print(i,end=" ")
#

lst=[4,-7,8,-1]
cl=filter(lambda x:x>0,lst)
for i in cl:print(i)