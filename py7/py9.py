def modify(lst):
    lst.append(10)
    print(id(lst),lst)
lst=[1,2,3]
print(id(lst),lst)
modify(lst)
print(id(lst),lst)
