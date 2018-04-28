class total:
	def __init__(self,x,y):
		self.num1=x
		self.num2=y
	def sum(self):
		print("1st number: ",self.num1)
		print("2nd number: ",self.num2)
		print("sum: ",self.num1+self.num2)
obj=total(10,20)
obj.sum()
obj=total(10.5,20.7)
obj.sum()