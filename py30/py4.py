#creating the thread are 3 ways in python
    #without using class
from threading import *
def display(x):
    print('hello, i am running!')
    print(x)
t = Thread()
t.start()

