class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        
    def show(self):
        print(self.m1,self.m2)
        
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        m3=(m1,m2)
        return m3
    
a = student(60,70)
b=student(66,76)
a.show()
b.show()
c=a+b
print(c)
