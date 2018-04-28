x=22 #global
def display():
    x=10   #local
    print(x)
    y=globals()['x']
    print(y) #global
display() #call the function
#print(x)  not available outside the fun
print(x)

'''
x=22 
def display():
    x=10   #local
    print(x)
    y=globals()['x']
    print(y) #global

display()
'''