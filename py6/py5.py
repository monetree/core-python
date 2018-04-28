#waf that return results of add, sub,mul,div
def cal(a,b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum,sub,mul,div;
x,y= [float(i) for i in input("enter the number to calculate: ").split(",")]
sum,sub,mul,div=cal(x,y)
print(sum)
print(sub)
print(mul)
print('%.2f'%div)