'''Create the custom Python classes which have methods and
attributes and implement single inheritance, multiple inheritance,
and multilevel inheritance'''

#Single Inheritance
class parent():
    def method(self):
        print("This is parent class")
class child(parent):
    def method1(self):
        print("This is child class")
obj=child()
obj.method()
obj.method1()

#Multiple Inheritance
class Father():
    def method(self):
        print("This is father's class")
class Mother():
    def method1(self):
        print("This is mother's class")
class child(Father,Mother):
    def method2(self):
        print("This is child class")
obj=child()
obj.method2()
obj.method1()
obj.method()

#Multilevel Inheritance
class Grandparent():
    def method(self):
        print("This is Grandparent's class")
class Parent():
    def method1(self):
        print("This is Parent's class")
class child(Grandparent,Parent):
    def method2(self):
        print("This is child class")
obj=child()
obj.method2()
obj.method1()
obj.method()
