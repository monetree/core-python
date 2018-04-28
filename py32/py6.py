#text widget with a vertical scroll bar
from tkinter import *
class Mymessage:
    def __init__(self,root):
        self.t = Text(root, width=20, height=6, font=('verdana',14,'bold'),fg='blue',bg='yellow',wrap=WORD)
        str = '''this is my first line\nthis is my 2nd line\nthis is my third line'''
        self.t.insert(END, str)
        self.t.pack(side = LEFT)
        self.v = Scrollbar(root, orient = VERTICAL,command=self.t.yview)
        self.t.configure = self.t.configure(yscrollcommand=self.v.set)
        self.v.pack(side=RIGHT, fill=Y)
root = Tk()
root.geometry('500x400')
root.title('my text and scoll bar')
mm = Mymessage(root)
root.mainloop()
