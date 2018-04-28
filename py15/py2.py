'''
    create a person class
'''
# #this is a class
# class person:
#     #properties or attribute
#     def __init__(self):
#         self.name='srinu'
#         self.age=22
#     #actions
#     def talk(self):
#         print('hello i am ', self.name)
#         print('age is', self.age)
# #create object
# p1=person()
# p1.talk()
# print(p1.name)
# print(p1.age)
class Person:
    def __init__(self,x):
        self.name=x
    def display(self):
        print('name is ',self.name)
obj=Person('srinu')
obj.display()