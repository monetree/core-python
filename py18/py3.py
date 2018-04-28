#using student class of student.py module
import py2
# from py2 import *
#create object
s=py2.student()
#store data into object
s.setId(10)
s.setName("jennifer")
s.setAddress("hno-12,newyork,usa")
s.setMarks(990)
#retrive data from the object
print('id= ',s.getId())
print('name= ',s.getName())
print('address= ',s.getAddress())
print('marks= ',s.getMarks())



