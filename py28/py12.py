
str = '1 nagesh, 11 vijay, 12 subbu, 13 anil'
import re
res = re.split(r'\d+', str)
print(res)