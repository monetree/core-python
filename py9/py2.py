#wapp fun to generate nos from m to n
def mygen(m,n):
    for i in range(m,n):
        while m<=n:
            yield m
            m+=1
#to generate no from 5 to 10
obj = mygen(5,10)
for i in obj:print(i)




def mygen(m,n):
    for i in range(m,n):
        while m<=n:
            print(m)
            m+=1
mygen(5,10)