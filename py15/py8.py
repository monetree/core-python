class total:
	def __init__(self,x,y):
		self.num1=x
		self.num2=y
	def sum(self):
		print("sum is: ",self.num1+self.num2)
x=int(input("enter the 1st no:"))
y=int(input("enter the 2nd no:"))
obj=total(x,y)
obj.sum()
