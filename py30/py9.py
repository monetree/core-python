#Multitasking -> executing multiple tasks at a time
from threading import *
from time import *
class Theater:
    def __init__(self,str):
        self.str = str
    def movietickets(self):
        for i in range(1,11):
            print(self.str,'for ticket no: ',i)
            sleep(1.5)
obj1 = Theater('cut ticket')
obj2 = Theater('show chair')
t1 = Thread(target=obj1.movietickets)
t2 = Thread(target=obj2.movietickets)
t1.start()
t2.start()




