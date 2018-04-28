#in inheritance all the members of superclass are available to sub class
'''
to refer to super class members from sub class, we can super()  method
ex:super().__init__()
super().method()
super().var
'''
#create square class and calculate area.DErive rectange class and calculate class
class square:
    def __init__(self,x):
        self.x=x
class rectangle(square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
    def area(self):
        print(self.x*self.y)
a,b=[float(x) for x in input("enter two no: ").split(',')]
r=rectangle(a,b)
r.area()

