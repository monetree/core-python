#create a generator that display even no from m to n

def mygen(m, n):
    if m%2 !=0:
        m+=1
    while m<=n:
        yield m
        m+=2
obj=mygen(10,20)
for i in obj:print(i)
