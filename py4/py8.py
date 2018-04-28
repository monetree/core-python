#enter a no and find it if it exist in a list
x=[10,20,30,40,50]
no=int(input("enter the number: "))
for i in x:
    if i==no:
        print("exist")
        break
else:
        print("not exist")
