from QssTestCases import  a

class A:
    def test_one(self):
        print("I am test 1")
    def __init__(self):
        print("I am Constructor")
        global a
        a =130302
        print(a)

class B():
    def test_two(self):
        print("I am Test B")

class C():
    def test_three(self):
        print("My Test 3")




obj = A()