#multiple Inhertance

class parent:
    def feature1(self):
        print('this is first feature')
    def feature2(self):
        print('this is second feature')
class child(parent):
    def feature3(self):
        print('this is third feature')
    def feature2(self):
        print('this is fourth feature')
class grandchild(child):
    def feature3(self):
        print('this is feature five')
a = grandchild()
a.feature1() 

b = child()
b.feature1()
