'''
a constructor is a special method that is useful to create and initialize the instance vars.
2 types
1.default constructor or zero parameterized constructor:is a constructor without any parameter.
2.parameteized constructor:is a constructor with 1 or more parameters

Aconstructor is a called at the timeof creating n object

'''
#create a student clas with roll no. name and marks in five subjects
class student:
    def __init__(self, r=0, n='',m=[]):   #default arguments
        self.rno=r
        self.name=n
        self.marks=m
    def display(self):
        print('roll no= ', self.rno)
        print('name= ', self.name)
        print('marks= ', self.marks)
        print('total marks= ', sum(self.marks))
s1=student(10,'srinu',[44,55,33,40,55])
s1.display()
s2=student(11,'vimala',[55,56,80,66,50])
s2.display()
s3=student()
s3.display()

