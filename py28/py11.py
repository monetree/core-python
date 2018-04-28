#split() -> breaks the string ->returns list
#Wa regular expression to split at the roll nos
str = '10 nagesh, 11 vijay, 12 subbu, 13 anil'
import re
res = re.split(r'\d\d', str)
print(res)
