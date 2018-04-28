#1.0
#read only first 10 characters
f = open('strings.txt','r')
str = f.read(10)
print(str)
f.close()
