#Wa regular exp to retrieve only names from the given string.
str = '10 nagesh, 11 vijay, 12 subbu, 13 anil'
import re
result = re.findall(r'\D\D\D\D\D\D\D',str)
print(result)

