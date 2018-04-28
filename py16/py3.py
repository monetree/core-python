'''types of methods is python
1.instance method
    a.accessor methods->these methods which access the instance vars. they do not modify.
    ->getXXX()
    b.mutator method->these methods which not oly access the instance vars but also modify them.
    ->setXXX()
2.class method
3.static method
'''
#create accessor and mutator method for employee class with id no and name
class employee(object):
    def setId(self,id):
        self.id=id
    def getId(self):
        return self.id
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
e1=employee()
e1.setId(10)
e1.setName('srk')
print('id= ',e1.getId())
print("name= ",e1.getName())



