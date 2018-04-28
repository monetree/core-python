'''
Date and time
epoch->elapsed time(in sec)
windows->1-1-current year midnight 12.00
linux->1-1-1970 midnight 12.00

'''
#To know the time elapsed
import time
epoch=time.time()
print('epochn time: ',epoch)
print('current time: ',time.ctime(epoch))

