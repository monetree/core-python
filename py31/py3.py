#Creating a frame in the root window
from tkinter import *
root = Tk()
root.geometry('500x400')
root.title('My frame')
f = Frame(root, width = 500, height=400, bg ='cyan')
f.pack()
root.mainloop()




