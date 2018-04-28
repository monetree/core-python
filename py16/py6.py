#wa static method that accept a no and returns itz square root value
import math
class myclass:
	@staticmethod
	def sqroot(x):
		return x**2
obj=myclass()
res=obj.sqroot(3)
print("square root is: ",res)