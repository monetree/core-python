#creating user-defined exceptions
class myException(Exception):
    def __init__(self,str):
        self.str=str

def check(dict):
    for k,v in dict.items():
        print('name= {} balance= {:.2f}'.format(k,v))
        if v<2000:
            raise myException('balance amout is less')
            break

try:
    bank={'raju':5600.00,'sita':8989.99,'vinay':6000.75,'gopi':1999.99,'vishal':8888.00}
    check(bank)
except Exception as e:
    print(e)
