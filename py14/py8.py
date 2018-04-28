#retrive only the first letter of each word in list
#normal code
words=['apple','grapes','papaya','pomogranames','banana']
lst=[]
for i in words:
    lst.append(i[0])
print(lst)

#list comp code
words=['apple','grapes','papaya','pomogranames','banana']
lst=[i[0] for i in words]
print(lst)