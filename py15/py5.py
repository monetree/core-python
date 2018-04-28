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
r=int(input("enter rno: "))
n=input("enter name: ")
m=[int(x) for x in input("enter marks").split(",")]
obj=student(r,n,m)
obj.display()
