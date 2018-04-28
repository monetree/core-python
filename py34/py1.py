#Alistbox is useful to display lst of items. The user can select 1 or more items
from tkinter import *
class Mylist:
    def __init__(self,root):
        self.f = Frame(root,width=800,height=400)
        self.f.pack()
        self.lb = Listbox(self.f,font="Arial 12 bold",fg='blue',bg='yellow',height=8,width=24,activestyle='underline',selectmode=MULTIPLE)
        self.lb.insert(0, 'California university')
        self.lb.insert(1, 'Texas A&M university')
        self.lb.insert(2, 'Berkley university')
        self.lb.insert(3, 'Oxford university')
        self.lb.insert(4, 'Cambridge university')
        self.lb.place(x=100, y=100)
        self.lb.bind('<<ListboxSelect>>', self.on_select)
        self.t = Text(self.f,width=30,height=8)
        self.t.place(x=400,y=100)
    def on_select(self,event):
        lst = []
        indexes = self.lb.curselection()
        for i in indexes:
            lst.append(self.lb.get(i))
        self.t.delete(0.0, END)
        self.t.insert(0.0, self.lst)

root = Tk()
ml = Mylist(root)
root.mainloop()




