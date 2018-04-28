#without stepsize
#normal
'''
lst=[]
for i in range(1,11):
    if i%2==0:
        lst.append(i)
print(lst)
'''
#list comp code
lst=[x for x in range(2,15) if x%2==0]
print(lst)
