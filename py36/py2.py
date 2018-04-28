#json to python
import json
with open('jsondata.txt','r') as f:
#data in json format in str
    str = f.read()
#converts data into python
d = json.loads(str)
#for specific records only
print(d)
if d['id'] ==10:
    print('name',d['name'])
