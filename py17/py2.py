#create a student class and dob as inner class
class student:
    def __init__(self):
        self.rno=10
        self.name="srk"
    def display(self):
        print("roll no: ",self.rno)
        print("name: ",self.name)
    class dob:
        def __init__(self):
            self.dd=3
            self.mm=1
            self.yy=1995
        def display(self):
            print('dob= {}/{}/{}'.format(self.dd,self.mm,self.yy))
s=student()
s.display()
d=student().dob()
# d=s.dob()
d.display()
