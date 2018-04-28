#2.0
#read using keyboard input
fname = input('enter filename: ')
f = open(fname, 'r')
str = f.read(10)
print(str)
f.close()
