#wapp to read a data from text file
f = open('myfile.txt','r')
str = f.read()
print(str)
f.close()
