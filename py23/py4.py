#to find the weekday of a date
from datetime import *
d,m,y=[int(x) for x in input("enter your date of birth (dd/mm/yyyy): ").split('/')]
dt=date(y,m,d)
print(dt)
str=dt.strftime('your birthday falls on %A\n and it is the %j th day')
print(str)

