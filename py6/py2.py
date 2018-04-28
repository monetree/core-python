#enter a group of no to display sum and avg

import sys
lst=sys.argv
n=len(lst)
print("no of elements= ",n-1)
sum=0
for i in range(1,n):
	sum+=float(lst[i])
print('sum=',sum)

print('average=',sum/(n-1))

#onle execute in terminal (system argument)