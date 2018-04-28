#class
from threading import *
class myclass(Thread):
    def run(self):
        print('i am running')
t = myclass()
t.start()
