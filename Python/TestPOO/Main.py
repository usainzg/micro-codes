# import User class from User file
from User import User
from User import Admin

# create user object from User class
user = User("unai", "usainzg", "unai1808")

# call sayHello() method from created object
user.sayHello()

# call User class method, equals to static method call on java
User.classMethod(6)

# call to __str__ method
print(user)

# test __eq__ overrided method
uObj = User("unai", "usainzg", "123456")
print(user == uObj)

# inheritanced class object
admin = Admin("admin", "admin", "admin123", "idAdmin")
admin.printId()