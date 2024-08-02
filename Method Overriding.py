class parent():
    def show(self):
        print('Inside a parent class')

class parent2():
    def display(self):
        print('Inside a Parent2 class')

class child(parent,parent2):
    def show(self):
        print('Inside a child class')

obj=child()
obj.show()
obj.display()
