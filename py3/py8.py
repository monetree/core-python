#accept a no from the keyboard and test wheather it is prime or not
# num = 9
# if num > 1:
#    # check for factors
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            print(i,"times",num//i,"is",num)
#            break
#    else:
#        print(num,"is a prime number")


num = int(input('enter a number: '))
if num > 1:
    for i in range(2,num):
        if(num % i) ==0:
            print('not')
            break
    else:
        print('prime ')
