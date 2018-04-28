#waf that accepts two strings and returns the total string
def join(s1,s2):
    return s1,s2;
x,y=[x for x in input("enter the name: ").split(",")]
x=x.strip()
y=y.strip()
res=join(x,y)
print('total string: ',res)