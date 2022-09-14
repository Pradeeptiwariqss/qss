from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def defMethod(self):
        pass
    # def nonAbsMethod(self):
    #     print("Concrete method method, now is abstract class")
    @abstractmethod
    def defMethod1(self):
        pass
 ##  Father is INTERFACE HERE
class Child(Father):
    def defMethod(self):
        print("it is a normal class and interface implemented here")
        print("For interface implementation same name method should create in impmented class")

    # def defMethod1(self):
    #     print("If in interface there are 2 method and you implement in class then you have to create two method in class then can create object of class")

# chillObj = Child()
# chillObj.defMethod()
# chillObj.defMethod1()

class grandChild(Child):
    def defMethod1(self):
        print("I can create object of grand child because there are two method inherit of interface, but we can not create ojb of child becasue both abs methods are not created in child")


gc = grandChild()
gc.defMethod1()
gc.defMethod()
