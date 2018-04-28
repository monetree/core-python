#wap to enter several no and find their sum and avg
lst=[float(x) for x in input("enter numbers:").split(',')]
s=sum(lst)
print('sum=', s)
n=len(lst)

print('avg', s/n)
