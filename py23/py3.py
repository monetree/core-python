'''dt=strftime('formatted string')
date,datetime
'''
#to display date no month no and year
#12th jan 2017
from datetime import *
dt=date.today()
print(dt)
str=dt.strftime('%dth %B %Y')
print(str)

