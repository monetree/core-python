# #wappp to deslay even nos from m to n
# m=int(input("enter the number: "))
# n=int(input("enter the number: "))
# while m<=n:
#     print(m)
#     m+=2
m=int(input('enter first no'))
n=int(input('enter second no'))
while m<=n:
    if m%2!=0:
        m+=1
    print(m)
    m+=2