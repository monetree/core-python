#call by value : call a fun and pass value
#call by fun:call a function and pass variable address(avl in c )

'''
call by object reference: call a function and pass object reference to that function
(only available is python)
1.if the object is immutable it can't be modified ex:str,tuple,frozenset
2.if the object is mutable it can be modified ex:list,dictionary,set
'''
def modify(str):
    str='hello'+str
    print(id(str),str)
str='ramu'
print(id(str),str)
modify(str)

