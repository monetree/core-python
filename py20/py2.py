'''
interfaces:An interface is an abstract class that contains all abstract methods only.

'''
#an interface that connect to any database
from abc import *
class myclass(ABC):
    @abstractmethod
    def connect(self):
        pass
class oracledb(myclass):
    def connect(self):
        print("connecting to oracle database ..")
class sybasedb(myclass):
    def connect(self):
        print("connnecting to sybase database..")
name=input("enter database name: ")
classname= globals()[name]
obj=classname()
obj.connect()


