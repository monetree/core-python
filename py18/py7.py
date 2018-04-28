#constructor in inheritane
class harry:
	def __init__(self):
		self.property=50000
	def display(self):
		print('property of harry: ',self.property)
class rosy(harry):
	pass
obj=rosy()
obj.display()