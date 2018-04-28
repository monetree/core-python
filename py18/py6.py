from py1 import teacher
class student(teacher):
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
