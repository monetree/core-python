# a=27
# b=4
# c=a//b
# print(c)
#
# a,b,c=1,2.5,'srk'
# print(a,b,c)
# print(a,b,c, sep=',')
# print(a,b,c, sep=':;---dhhd55dbbd41d//-')
# print(a,b,c, sep='')
#
# x=y=z=10
# print(x,y,z, sep=',')
#
# #arthmatic operator
# x=5
# x+=1
# print(x)
# x-=1
# print(x)
# x*=1
# print(x)
#
# x=21
# x/=4
# print(x)
# x=21
# x//=4
# print(x)
# x=23
# x//=4
# print(x)
#
# x=1
# x=-x
# print(x)
# x=-1
# x=-x
# print(x)
# x=-1
# x=x
# print(x)
# x=1
# x=x
# print(x)
#
# #boolean operator
# print(1<2<3)
# print(3>2>1)
# print(1>2>3)
# print(1<2>3)
#
# a=True
# b=False
# print(type(a))
# print(type(b))
# print(a and b)
# print(a or b)
# print(a and a)
# print(b and b)
# print(not(b))
# print(not(a))
#
# print()
# print('hello pyy')

a,b=10,11
print('hello',a,b,sep=',')

name='srk'
print('hello',name)
print('hello'+name)

salary=5000.55
print('your salary',salary)

name='srk'
print(type(name))

name='srk'
sal=5000.999
print('hello',name,'your salary',sal)

print('hello %s your salary %f' %(name,sal))

print('hello %s your salary %10.2f' %(name,sal))

print('hello {} your salary {}'.format(name, sal))

print('hello {0} your salary {1}'.format(name, sal))

print('hello {1} your salary {0}'.format(name, sal))

print('hello {:s} your salary {:.2f}'.format(name,sal))
