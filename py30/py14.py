#thead dead lock
from threading import *
from time import *
l1 = Lock()
l2 = Lock()
def bookticket():
    l1.acquire()
    print('bookticket Locked train')
    sleep(1)
    print('booktickets wants to jump into compartment')
    l2.acquire()
    print('bookticket locked compartment')
    l2.release()
    l1.release()
    print('booking ticket is done')
def cancelticket():
    l2.acquire()
    print('cancel ticket locked comparment')
    sleep(2.5)
    print('cancel ticket wants to jump into train')
    l1.acquire()
    print('cancel ticket locked train')
    l1.release()
    l2.release()
    print('cancellation is done')
t1=Thread(target=bookticket)
t2=Thread(target=cancelticket)
t1.start()
t2.start()


