#wapp to test wheather a given no is even or odd
num=int(input("enter no to check: "))
if num==0:
    print(num,'is zero')
elif num%2==0:
    # print (num,"is even")
    print('{:d} is even'.format(num))
else:
    print(num,'is odd')