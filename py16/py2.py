class myclass:
    n=0
    @classmethod
    def modify(cls):
        cls.n+=10
m1=myclass()
m2=myclass()
print(m1.n,m2.n)
m1.modify()
print(m1.n,m2.n)
m1.n+=1
print(m1.n,m2.n)

#1.if a class var is modified in the class namespace, it will affect all the objects.
#2.if a class var is modified in the instance namespace, then it will affect only that object.
