#sub() -> substitute another string in the place of original string. -> modified original strings.
#wa regular expression to replace 'Ahmedabad' with 'Allahabad'
str = 'Kumbhamela will be conducted at Ahmedabad in india'
import re
str = re.sub(r'Ahmedabad','Allahabad',str)
print(str)
