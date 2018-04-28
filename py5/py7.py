'''assert statement: to conform wheather the input
 is according to a given condition or not.
syn:assert condition,'message'
ex: asset x>5,'wrong input'

Assersion error:wrong input outside of thr range
'''
#wapp to accept inputs in the range of (10,20)
n=int(input("enter a number: "))
assert n>=10 and n<=20, 'wrong input'
print('u entered: ',n)

