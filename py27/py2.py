#wap to zip a group of files
from zipfile import *
z = ZipFile('test.zip', 'w', ZIP_DEFLATED)
z.write('1.html')
z.write('2.html')
z.write('3.html')
z.close()

