#To find the future date
from datetime import *
dt=datetime(2017,12,5,10,30)
duration=timedelta(weeks=1, days=25, hours=10, minutes=32)
print('new date time: ',dt+duration)
