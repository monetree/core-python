my=[10,2,30]
del(my[2]) #delete "defined value" from the array
print(my)

my.remove(2) #delete "defined value" from the array
print(my)     #both del and remove same

my=[1,2,3,4,5]
my.remove(2)
print (my)

my=[10,20,30]
del my [:] #my.clear() not supported on pythen soe desired version so use instead this to chear entire array value
print(my)

lst=[1,2,3,4]
lst[0]=22 #put the the desired value byreplacing it from array
print(lst[0])

lst[1:4]=5,7
print(lst[1:4])

print(max(lst)) #max and value in the array
print(min(lst))

lst=[1,2,3,4,5]
print(len(lst))

lst=[1,1,2,2,2,3,4,4]
print(lst.index(2)) #on which no of place it is 'count from 0-1-2'

lst.append([40])
print(lst) #add a new value in a array

print(lst.count(4)) #how many times it is available in the array

lst.insert(0,12)
print(lst) # inset desired value in the desired position '12 in 0 no of place'


lst=[1,5,2,44,2,3,4,4]
lst.sort() #assending
print(lst)

lst.sort(reverse=True)
print(lst) #decending

lst=[1,5,2,44,2,3,4,4]
lst.reverse() #reversing order
print(lst)

t=() #tupple
print(t)

t=(10,)
print(t)

t=(10,40,20,11,10,5)
print(t)

print(sorted(t))  #assending

print(sorted(t, reverse=True)) #decendig

print(t.count(10)) #count the value how many times is available

r=range(5)
print(r)

for i in r:print(i)
print(i)

num=range(10,20)
for i in num:print(i)
for n in range(10,30,2):print(n)#show to 10-30 by 2 difference
for x in range(5,0,-1):print(x) #count five to zero reverse