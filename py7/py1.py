#local and global vars
x=12
def display():
    x=10   #local
    print(x)
display() #call the function
#print(x)  not available outside the fun
print(x)