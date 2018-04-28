#push button using class
from tkinter import *
class MyButtons:
    def __init__(self, root):
        self.f = Frame(root, width =600, height=500)
        self.f.pack()
        self.b1 = Button(self.f, text='my Button',width=20,height=2,bg='yellow',fg='blue',command=self.clickme)
        self.b2 = Button(self.f, text='Exit',width=20,height=2,command=quit)
        self.b1.grid(row=0,column=0)
        self.b2.grid(row=1,column=0)
    def clickme(self):
        self.lbl = Label(self.f, text="hello you clicked me !", width=30,height=2,font=('Arial',30,'italic bold'),fg='goldenrod')
        self.lbl.grid(row=2,column=0)
root=Tk()
root.title('My push button')
root.geometry('600x500')
mb = MyButtons(root)
root.mainloop()

