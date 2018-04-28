#Wa regular exp to retrieve only roll nos from the given string.
str = '10 nagesh, 11 vijay, 12 subbu, 13 anil'
import re
result = re.findall(r'\d\d',str)
print(result)

