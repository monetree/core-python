#single tasking -> executing onetask at a time
#preparation of tea
from threading import *
from time import *
class myclass:
    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()
    def task1(self):
        print('boil milk + tea powder for 5 min')
        sleep(5)
    def task2(self):
        print('add sugar and boil for another 2 min')
        sleep(2)
    def task3(self):
        print('filter and serve it')
obj = myclass()
t = Thread(target=obj.prepareTea)
t.start()


