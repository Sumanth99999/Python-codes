class computer:
    def __init__(self,brand,processor,ram,rom):
        self.brand=brand
        self.processor=processor
        self.ram=ram
        self.rom=rom
    def compare(self,other):
        if self.processor==other.processor:
            return True
        else:
            return False
        
obj1=computer('apple','silicon',8,256)
obj2=computer('hp','amd','8','256')
print(obj1.brand,obj1.processor,obj1.ram)
print(obj2.brand,obj2.processor,obj2.ram)

#using compare function to check the data in two objects

if obj1.compare(obj2):
    print('same')
else:
    print('diff')
        
        
