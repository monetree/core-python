# #set (set represents unordered collection of data)
# #{write in flower brackets}
# #indexing,slicing,repet not possible in set
# s={10,20,20.5,'kiran','x'}
# # print(s)
# #
# # for x in s:print(x)
# #
# # print(s)
# s.update([66,77])
# print (s)
#
# s.remove(77)
# print(s)
#
# #s[0] (it is not suppoted in set)
#
# #frozenset same as set
# fs=frozenset(s)
# print(fs)
#
# ''' frozenset has no attribute remove
# fs.remove(66)
# print(fs)
# so it will show error'''
#
# '''frozen set object doesnot support indexing
# print(fs[0])
# so agaain it will show error'''

#map:map represents elements in the form of key value pairs
d={10:'ramu',11:'vani',12:'sita',13:'rao'}
# k=d.keys()
# for x in k:print(x)

# v=d.values()
# for i in v:print(i)

# obj=d.items()
# for k,v in obj:print(k, ' ',v)

# print(d[10])

# d[10]='krishna'
# print(d)

# del(d[11])
# print(d)

marks={'tom':[33,44,55],'ram':[30,40,60]}
print(marks)

print(marks['tom'])

print(marks['tom'][0])

print(marks['tom'][2])

print(type(marks))


