import time, datetime
t=time.ctime()
print('current date and time: ',t)

t2=datetime.datetime.today()
print('current date: {}/{}/{}'.format(t2.day,t2.month,t2.year))
print('current time: {}:{}:{}'.format(t2.hour,t2.minute,t2.second))

t3=datetime.datetime.now()
print('current date: {}/{}/{}'.format(t3.day,t3.month,t3.year))
print('current time: {}:{}'.format(t3.hour,t3.minute))


