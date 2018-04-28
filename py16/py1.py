'''
types of variables
1.instance variable : is a variable whose separate copy is available to all the objects.
(self.var) ref name of variables
2.static vars/class variables: is a variable whose single copy is shared by all the objects.

'''
class myclass:
    n=0
    @classmethod
    def modify(cls):
        cls.n+=10static vars
m1=myclass()
m2=myclass()
print(m1.n,m2.n)

m2.n+=1
print(m1.n,m2.n) #modify class var in instance namespace

m2.modify()
#modify class var in class namespace
print(m1.n,m2.n)

