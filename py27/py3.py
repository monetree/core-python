# To unzip the contents of a zipped file
from zipfile import *
z = ZipFile('test.zip', 'r')
z.extractall('cd /Downloads/')
z.close()
