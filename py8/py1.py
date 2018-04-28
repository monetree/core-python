#recursive function: a fun written inside another function
#a function calling itself is recursive fun
#less code

'''
if n==0,res=1
else fact(n)=n*fact(n-1)
'''

#recursive fun to calculate factorial value
def fact(n):
    if n==0:
        res=1
    else:
        res=n*fact(n-1)
    return res
n=int(input('enter a number: '))
result=fact(n)
print('fact is',result)

'''
def fact(n)=n is parameter or formal argument-declared in the function
fact(4):actual argument-passed to the function
'''
