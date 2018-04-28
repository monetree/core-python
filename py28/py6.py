import re
str ='man sun mop run'
regex = 'm\w\w'
res = re.match(regex, str)
if(res):
    print(res.group())
else:
    print('not found')
