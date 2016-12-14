# user class definition
class User:
    # constructor
    # before call to __init__ method, the __new__ method is called
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    # private method
    def _private(self):
        print("Private method")
    
    # normal method
    def sayHello(self):
        print("My name is {0}".format(self.name))

    # class method , equals static method on java
    @classmethod
    def classMethod(cls, param):
        print("Parametro: {0}".format(param))

    # override __str__ method
    def __str__(self):
        return("My name is {0}, my username is {1} and my password is {2}".format(self.name, self.username, self.password))

    # override __eq__ method: equals method
    def __eq__(self, obj):
        return obj.username == self.username


class Admin(User):
    def __init__(self, name, username, password, adminId):
        self.name = name
        self.username = username
        self.password = password
        self.adminId = adminId
    
    def printId(self):
        print(self.adminId)