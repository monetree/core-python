#wapp to store group of characters into a text file
f = open('myfile.txt','a')
chars = input('enter chars: ')
f.write(chars)
f.close()
