'''instance vars are the variables which are created in the object
syn: self.var
instance methods re the methods that act on instance vars:
syn:def method(self):
instnce methods are called as:
obj.method()
'''
#create a student clas with roll no. name and marks.
class student:
    def __init__(self):
        self.name='srk'
        self.roll_no=10
        self.mark=500
    def display(self):
        print('hello my name is', self.name)
        print('hello my roll no', self.roll_no)
        print('hello my mark is', self.mark)
s1=student()
s1.display()
print(s1.name)
print(s1.roll_no)
print(s1.mark)



