import re
str ='ant man sun mop run'
regex = 'm\w\w'
res = re.findall(regex, str)
print(res)
