#write a regax to check wheather a string is starting with he or not
import re
str = 'hello world'
res = re.search(r'ld$',str)
if res:
    print('yes it is starting with ld')
else:
    print('no it is not starting with ld')
