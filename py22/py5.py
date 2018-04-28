'''
A log file is a file that contains description of error and exceptions.
storing the errors/exceptions in a log file is called 'logging'.
Logging is useful in software testing.

'''
'''
Logging the exceptions
'''
import logging
logging.basicConfig(filename='mylog.txt',level=logging.ERROR)
try:
    a,b=[int(x) for x in input('enter two number: ').split(',')]
    c=a/b
except Exception as e:
    logging.exception(e)
else:
    print("result of division is= ",c)
