#4.0
#using importing sys, os
import sys, os
fname = input("enter filename: ")
if os.path.isfile(fname):
    f = open(fname,'r')
else:
    print('file does not exist')
    sys.exit()

str = f.read()
print(str)
f.close()
