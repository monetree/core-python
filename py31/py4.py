#Creating a push button in the root window
from tkinter import *
root = Tk()
root.geometry('600x500')
root.title('My push button')
def click(self):
    print('hello you clicked me.')
f = Frame(root, width=700, height=600, bg='cyan')
f.pack()
b = Button(f, width = 20, height=2, text ='My button', fg = 'red', bg ='lime',
           activeforeground = 'blue',activebackground='pink',font=('Georgia',-20,'italic underline'))     #height=2( 2 row height),width 20 character width
b.pack()
b.bind('<Button-1>',click)#mouse left button for Button -1
root.mainloop()



