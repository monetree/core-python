#it is possiblle to pass a function as parameter to another function
def display(fun):
    return "hello"+fun() #result of fun function will concatinate with hello
def fun():
    return ' krish'
x=display(fun)
print(x)
