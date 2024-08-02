#Single Inheritance
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
a = parent()
a.feature1() 
a.feature2()

b = child()
b.feature1()
b.feature2()
b.feature3()








        
        
