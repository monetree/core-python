#method overloading :same method performing various task
class myclass:
    def add(self,a=0,b=0,c=0,d=0):
        x=a+b+c+d
        print('sum= ',x)
m=myclass()
m.add(10,11)
m.add(10,11,25)
m.add(10,11,25,40)
m.add()

