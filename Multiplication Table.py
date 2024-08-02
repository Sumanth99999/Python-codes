def Multiplication_table():
    a = int(input("which table do you need?"))
    b = int(input('Enter range:'))
    for i in range(1,b):
        print(a, 'x', i,"=", a*i)
    print()
    
Multiplication_table()
    
