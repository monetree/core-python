# python to json
import json
employee = eval(input('enter data in {} '))
str = json.dumps(employee) #covert employee object to json string
#store it to text file
with open('jsondata.txt','w') as f:
    f.write(str)
