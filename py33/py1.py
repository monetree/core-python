#display course names in check box
from tkinter import *
class Mycheck:
    def __init__(self,root):
        self.f = Frame(root,width=500,height=400)
        self.f.pack()
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.c1 = Checkbutton(self.f,bg='yellow',fg='green',font=('Georgia',-20,'underline'),
                            text='java',variable=self.var1,command=self.display)
        self.c2 = Checkbutton(self.f, bg='cyan', fg='red', font=('Georgia', -10, 'underline'),
                              text='python', variable=self.var2, command=self.display)
        self.c3 = Checkbutton(self.f, bg='pink', fg='blue', font=('Georgia', -20, 'bold'),
                              text='devops', variable=self.var3, command=self.display)
        self.c1.place(x=100,y=100)
        self.c2.place(x=100, y=160)
        self.c3.place(x=100, y=220)
    def display(self):
        x = self.var1.get()
        y = self.var2.get()
        z = self.var3.get()
        str=' '
        if x==1: str+='java'
        if y==1: str+='python'
        if z==1: str+='devops'
        self.lbl = Label(self.f, text=str)
        self.lbl.place(x=100, y=300)

root = Tk()
root.geometry('500x400')
mc = Mycheck(root)
root.mainloop()

