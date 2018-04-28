#This a file to store names and phone numbers.
n = int(input("how many: "))
with open('phones.dat','wb') as f:
    for i in range(n):
        name = input("enter name: ")
        no = input("enter phone no: ")
        name = name.encode()
        no = no.encode()
        f.write(name+no+b"\n")
