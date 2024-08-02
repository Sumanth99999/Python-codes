def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-2)+fibonacci(i-1)
a=int(input('Enter Range: '))
for i in range(a):
    print(fibonacci(i))
        
    
