#Wap regex to search for strings starting with m and having 3 characters.
import re
str ='ant man sun mop run'
regex = 'm\w\w'
res = re.search(regex, str)
if res:
    print(res.group())

#search -> first accourance of the string -> group()
#find all -> returns all  strings -> list
#match -> searches only in the beginning of the string -> group()

