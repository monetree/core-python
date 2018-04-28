#generator:a generator is a function that generates a sequence of numbers.generator uses yield statement

#wapp fun to generate nos from m to n
def mygen(m,n):
    for i in range(m,n):
        while m<=n:
            print(m)
            m+=1
#to generate no from 5 to 10
mygen(5,10)