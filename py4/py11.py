#position of the number
# list=[10,20,30,40]
# num=int(input("enter number: "))
# pos=0
#
# len=len(list)
#
# for i in list:
# 	pos+=1
# 	if num==i:
# 		print("{} is at {} position".format(num,pos))
# 		break
# else:
# 	print("number doesn't exist in the list")
#
#
list=[10,20,30,40]
num=int(input("enter: "))
pos=0
for i in list:
	pos += 1
	if i==num:
		print("{} is at {} position".format(num,pos))
		break
else:
	print('not')



