#defining global and local variables
a = 10 #global variable
def fun():
    a=15 #local variable
    print(a)
fun()
print(a)


#using global variable 
a= 10
def fun():
    global a
    a=15
    print(a)
fun()
print(a)


#using both global and local variables
a = 10
def fun():
    a = 15
    print(a)
    x= globals()['a']
    print(a)
fun()
print(a)
