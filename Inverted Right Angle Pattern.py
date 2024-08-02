def inverted(a):
    for i in range(a,0,-1):
        print(i*'*')
a = int(input('Enter the number of lines:'))
inverted(a)
