def swapping(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)

a=int(input('Enter first value: '))
b=int(input('Enter second value: '))
swapping(a,b)
