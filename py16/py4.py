''' static methods:act on static vars / class vars.
used where?
1.to perform temporary calculations
2.to set environment vars
3.to count no. of objects
'''
# wap to count no of objects in a class
class myclass:
    count=0
    def __init__(self):
        myclass.count+=1
    @staticmethod
    def noObjects():
        print('no of objects= ',myclass.count)
obj1=myclass()
obj2=myclass()
obj3=myclass()
myclass.noObjects()



#
# class person:
#     age=25
#     def ageis(cls):
#         print('age is ',cls.age)
#
# person.ageis=classmethod(person.ageis)
# person.ageis()


# class math:
#     def add(x,y):
#         return x+y
# math.add=staticmethod(math.add)
# print('sum is ',math.add(10,20))
#

