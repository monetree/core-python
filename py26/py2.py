#Random Accessing
with open('line.txt','w+b') as f:
    f.write(b'Python is Amazing')
    n = f.tell()
    print(n)
    f.seek(0,0)
    print(f.read(5))
    f.seek(-5,2)
    print(f.tell())
    print(f.read(5))
    print(f.tell())

'''
a m a z i n g   p y  t  h  o  n
1 2 3 4 5 6 7 8 9 10 11 12 13 14
14131211109 8 7 6 5   4  3  2  1

'''

