#lebels and entry boxes
from tkinter import *
class Myentry:
    def __init__(self,root):
        self.f = Frame(root,width=500, height=400)
        self.f.pack()
        self.l1 = Label(text = 'enter your name: ')
        self.l2 = Label(text = 'enter your password: ')
        self.e1 = Entry(self.f,width=20,fg='blue',bg='yellow',font=('Arial',14))
        self.e2 = Entry(self.f, width=20, fg='red', bg='cyan', font=('Arial', 14),show='*')
        self.l1.place(x=50,y=100)
        self.e1.place(x=300,y=100)
        self.l2.place(x=50,y=160)
        self.e2.place(x=300,y=160)
        self.e2.bind('<Return>',self.display)
    def display(self,event):
        s1 = self.e1.get()
        s2 = self.e2.get()
        self.lbl = Label(self.f, text=s1+' '+s2)
        self.lbl.place(x=50,y=200)
root = Tk()
root.title("my lebel and checkbox")
me = Myentry(root)
root.mainloop()
