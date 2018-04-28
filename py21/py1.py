#divide two number and store the result into a file -v1.0

# f=open('testfile.txt','w')
# a,b=[int(x) for x in input("enter two number: ").split(",")]
# c=a/b
# f.write("writting %.2f into the file."%c)
# f.close()
# print('file closed')

#an exception is a runtime arror that can be handled by the programmer.
#when there is a exception, the program terminates abnormally.
'''the files and dbs are not closed
1.the data in those files and dbs will be deleted
2.software may be corrupted.
'''

f=open('testfile.txt','w')
a,b=[int(x) for x in input('enter nos ').split(',')]
c=a+b
f.write('sum of {} and {} is {}'.format(a,b,c))
f.close()
