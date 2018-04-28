#abstraction
class bank:
    def __init__(self):
        self.accno = 1001
        self.name = 'nages'
        self.bal = 8000.50
        self.__loan = 500000.00
        #__ before variable means private
    def display_to_clerk(self):
        print('accno= ',self.accno)
        print('name= ',self.name)
        print('bal= ',self.bal)
        print('loan= ',self.__loan)
b=bank()
b.display_to_clerk()

print(b.accno)
print(b.name)
print(b.bal)
#print(b.loan)
print(b._bank__loan) #name mangling: is a technique to using class name before variable name differently.
#name mangling is useful for access the private vars.
'''
syn: obj._classname__variablename
'''
