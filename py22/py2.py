#To handle assertionError exception -v2.0
try:
    n=int(input("enter a number between 5  and 10: "))
    assert n>5 and n<10, 'wrong input entered'
    print("u entered: ",n)
except AssertionError as obj:
    print(obj)
