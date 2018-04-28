#using an independent class
from threading import *
class myclass:
    def display(self):
        print('hello m runnning!')
obj=myclass()
t=Thread(target=obj.display)
t.start()
