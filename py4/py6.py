#find sum of list of no without using sum function
lst=[int(i) for i in input("enter nos: ").split(",")]
sum=0
for x in lst:
    sum+=x
print(sum)

