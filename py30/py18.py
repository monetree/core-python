from threading import *
from time import *
from queue import *
class producer:
    def __init__(self):
        self.q = Queue()
    def produce(self):
        for i in range(1,10):
            self.q.put(i)
            sleep(1)
            print('Item produced')
class consumer:
    def __init__(self,prod):
        self.prod = prod
    def consume(self):
        for i in range(1,11):
            print('Receieved: ',self.prod.q.get(i))
p = producer()
c = consumer(p)
t1 = Thread(target = p.produce)
t2 = Thread(target = c.consume)
t1.start()
t2.start()

