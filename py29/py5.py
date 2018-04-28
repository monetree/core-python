#write a reg exp to retrive data from a html page
import re
import urllib.request
f = urllib.request.urlopen(r'file:///home/soubhagya/PycharmProjects/py29/py.html',)
str = f.read()
str = str.decode()  # convert from byte sto str
#print(str)
regex = r'<td>\w</td>\s<td>(\w+)</td>\s<td>(\d\d.\d\d)</td>'
# regex1 = r'<td>(\d\d)</td>'
# regex2 = r'<td>(\D+)</td>'

res=re.findall(regex, str)
print(res)
