#write a regax to retrive date of births from a given string
import re
str = 'vijay 20 1-5-2001, Rohit 21 22-10-1990,Sita 22 15-09-2000'
res = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(res)
