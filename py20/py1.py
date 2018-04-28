''''
concrete method: method with body
abstract method : method without body-> when each object want to perform diff task we need abstract class
abstract class: that contains abstract methods.
'''
#abstract class
from abc import ABC, abstractmethod
class myclass(ABC):
    @abstractmethod
    def calculate(self,x):
        pass
class sub1(myclass):
    def calculate(self,x):
        print("square value = ",x*x)
import math
class sub2(myclass):
    def calculate(self,x):
        print("square root= ",math.sqrt(x))
s1=sub1()
s1.calculate(16)
s2=sub2()
s2.calculate(16)




