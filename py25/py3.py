#Pickle - serialization
import pickle, py2
f = open('emp.dat','wb')
n = int(input('how many records? : '))
for i in range(n):
    id = int(input("enter id no: "))
    name = input("enter name: ")
    sal = float(input("enter sal: "))
    e = py2.emp(id,name,sal)    #class name emp module py2
    pickle.dump(e, f)
f.close()
