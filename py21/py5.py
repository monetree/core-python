#divide two number and store the result into a file -v5.0
try:
    f=open('testfile.txt','w')
    a,b=[int(x) for x in input("enter two number: ").split(",")]
    c=a/b
except ZeroDivisionError as obj:
    print(obj)
except ValueError:
    print("please type only integers")
else:
    f.write("writting %.2f into the file." % c)
finally:
    f.close()
    print('file closed')
