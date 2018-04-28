#variable length arguments:that can accept zero or more values
def sum1(*arg):
    print('sum= ',sum(arg))
sum1(10,11)
sum1(1,2,3,5,5,5,8)
sum1()

