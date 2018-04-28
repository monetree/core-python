#wapp to store a group of strings into a text file.
f = open('strings.txt','w')
str = input("enter string (@ at end): ")
while str != '@':
    if str != '@':
        f.write(str+"\n")
    str = input()
f.close()
