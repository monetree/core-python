#when multiple threads act on 1 or more objects simultaneously, then the result will not be reliable.
#two threads acting on same object
from threading import *
from time import *
class railway:
    def __init__(self, available):
        self.available = available
        self.l = Lock()
    def reserve(self,wanted):
        self.l.acquire()
        print('no of berths available= ',self.available)
        if self.available >= wanted:
            name = current_thread().getName()
            print(wanted,"berths allorted ", name)
            #time delay for ticket printing
            sleep(2)
            self.available-=wanted
        else:
            print('no berths to allot')
        self.l.release()
obj = railway(1) #here 1 is available no of berths
t1 = Thread(target = obj.reserve, args=(1,))
t2 = Thread(target = obj.reserve, args=(1,))
t1.setName('first person')
t2.setName('second person')
t1.start()
t2.start()