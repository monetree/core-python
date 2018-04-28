#to know if  a file exists or not
#3.0
#using exception handling concept
try:
    fname = input('enter filename: ')
    f = open(fname, 'r')
    str = f.read(10)
    print(str)
    f.close()
except FileNotFoundError:
    print('sorry, file does not exist')
