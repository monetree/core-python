#positional argument-arguments opassed in correct order
def display(name,price):
    print('name= {}\nPrice= {:.2f}'.format(name,price))
display('tomato',45.50) #positional arguments

#keyword arguments:which identifies the parameters by their name
def grocery(item,price):
    print('item=%s\nPrice=%.2f'%(item,price))
grocery(item='tomato',price=45.50)
