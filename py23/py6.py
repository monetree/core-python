#wapp to sort a given group of dates
from datetime import *
lst=[]
n=int(input("how many dates? :"))
for i in range(n):
    d,m,y=[int(x) for x in input("enter date(dd/mm/yyyy): ").split('/')]
    dt=date(y,m,d)
    lst.append(dt)
lst.sort()
for i in lst:print(i)