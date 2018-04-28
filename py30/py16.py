#thread communication using notify() and wait()
from threading import *
from time import *
class producer:
    def __init__(self):
        self.lst=[]
        self.cv = Condition()
    def produce(self):
        self.cv.acquire()
        for i in range(1,11):
            sleep(1)
            self.lst.append(i)
            print('item produced..')
        self.cv.notify()
        self.cv.release()
class consumer:
    def __init__(self,prod):
        self.prod = prod
    def consume(self):
        self.prod.cv.acquire()
        self.prod.cv.wait(timeout=0)
        self.prod.cv.release()
        print(self.prod.lst)
p = producer()
c = consumer(p)
t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)
t1.start()
t2.start()
