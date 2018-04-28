lst=[float(x) for x in input("enter nos: ").split(',')]
n=len(lst)
s=sum(lst)
a=s/n
print('sum= {}\nAverage= {:.2f}'.format(s,a))
