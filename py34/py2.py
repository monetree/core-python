#Menu
from tkinter import *
class Mymenu:
    def __init__(self,root):
        self.menubar = Menu(root)
        root.config(menu=self.menubar)
        self.filemenu = Menu(root, tearoff=1)
        self.filemenu.add_command(label="New",command=self.donothing)
        self.filemenu.add_command(label="Open", command=self.donothing)
        self.filemenu.add_command(label="Save", command=self.donothing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=root.destroy)
        self.menubar.add_cascade(label="file",menu=self.filemenu)
        self.editmenu = Menu(root,tearoff=0)
        self.editmenu.add_command(label="cut",command=self.donothing)
        self.editmenu.add_command(label="copy", command=self.donothing)
        self.editmenu.add_command(label="paste", command=self.donothing)
        self.menubar.add_cascade(label="edit",menu=self.editmenu)
    def donothing(self):
        pass
root = Tk()
root.geometry('500x450')
root.title('my menu')
mm=Mymenu(root)
root.mainloop()


