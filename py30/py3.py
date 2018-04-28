#creating the thread are 3 ways in python
    #without using class
from threading import *
def display():
    print('hello, i am running!')
t = Thread(target=display)
t.start()
