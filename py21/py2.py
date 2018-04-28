'''
1.write the code inside try block->try block prevents abnormal termination
2.write messages in the except block
3.close the files and dbs in the finally block
performing this task is called exception handling
'''
#divide two number and store the result into a file -v2.0

try:
    file=open('testfile.txt','w')
    a,b=[int(x) for x in input("enter two number: ").split(",")]
    c=a/b
    file.write("writting %.2f into the file." % c)
except ZeroDivisionError:
    print('division by zero happened')
    print('please do not type zero in input')
finally:
    file.close()
    print('file closed')
