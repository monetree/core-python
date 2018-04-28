from time import *
t1=perf_counter()

i,sum=0, 0
while(i<100):
	sum+=i
	print(sum)
	i+=1
sleep(3)
t2=perf_counter()
print('Execution time %f seconds '%(t2-t1))