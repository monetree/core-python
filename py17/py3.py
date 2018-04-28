#create a student class and dob as inner class
class student:
    def __init__(self,rno,name):
        self.rno=rno
        self.name=name
    def display(self):
        print("roll no: ",self.rno)
        print("name: ",self.name)
    class dob:
        def __init__(self,dd,mm,yy):
            self.dd=dd
            self.mm=mm
            self.yy=yy
        def display(self):
            print('dob= {}/{}/{}'.format(self.dd,self.mm,self.yy))
s=student(100,'viswa')
s.display()
#d=student.dob(10,10,1989)
d=s.dob(10,10,1989)
d.display()
