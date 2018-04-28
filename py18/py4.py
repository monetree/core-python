from py1 import teacher
class student(teacher):
    # student class id called derived class and py1 is super class
    # syn: subclass(superclass)
    # inheritance: deriving new class from existing classes
    # all the features of existing classes are available to the new classes.
    #code reusability is the main advantages of inheritance.
    #theproductivity of the programmer is increased
    #it will improve the overall productivity of the company.
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
obj=student()
obj.setId(45)
obj.setName("britney")
obj.setAddress("tokiyo")
obj.setSal("40000")
obj.setMarks(456)
print("Id: ",obj.getId())
print("Name: ",obj.getName())
print("Address: ",obj.getAddress())
print("Salary: ",obj.getSal())
print("Marks: ",obj.getMarks())

