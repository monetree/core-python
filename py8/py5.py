#function decorator: is a function that takes fun as argument and returns a function
#use:to decorate (modify) the result given by a function

#write a function decorator to increment the result of another function by 2
def decor(fun):
    def inner():
        res=fun()
        return res+2
    return inner
#this is another fun to which decor is applied
def num():
    return 10
#apply decor function to num()
f=decor(num) #f contains inner function name
res=f()
print(res)
