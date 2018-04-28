#Operation on mmap file
import mmap, sys
#Convert the fileinto mmap file
f = open('phones.dat','r+b')
mm = mmap.mmap(f.fileno(),0)
#Menu
print('1 display all entries')
print('2 find the phone no')
print('3 change the phone no')
print('4 Exit')
ch = input('Your choice: ')
if ch=='4':
    sys.exit()
if ch=='1':
    data = mm.read()
    print(data.decode())
if ch == '2':
    name = input("enter name: ")
    n = mm.find(name.encode())
    n1 = n+len(name)
    no = mm[n1: n1+10]
    print("phone no: ",no.decode())
if ch == '3':
    name = input('enter name: ')
    n = mm.find(name.encode())
    n1 = n+len(name)
    no = input('enter new phone no: ')
    mm[n1:n1+10] = no.encode()
    print(' phone no changed ... ')
