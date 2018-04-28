#A thread is a individual process of execution
#a Thread always executes statements
#write a python prog to know the thread name which is running a python programme.
import threading
print('i am the first line')
str = threading.current_thread().getName()
print('currently running thread = ', str)
if threading.current_thread() == threading.main_thread():
    print('it is main thread')
else:
    print('no')
#Every python prog is executed by an internal thread called main thread
